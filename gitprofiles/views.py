from django.http import HttpResponse
from .forms import SearchForm, ProfileForms
from django.forms import formset_factory
from django.shortcuts import render
from django.utils import timezone
from .gitSearch import GitObj
from .models import Profiles
# Create your views here.

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            location = form.cleaned_data['location']
            language = form.cleaned_data['language']
            repos = form.cleaned_data['repos']
            followers = form.cleaned_data['followers']

            profiles = GitObj()
            profiles = profiles.gitSearchProsForHire(location, language, repos, followers)
            ProfileFormset = formset_factory(ProfileForms,  extra=0)

            profiles_list = []

            for profile in profiles:
                langs = [None, None, None]
                for l,i in zip(profile.type,range(len(profile.type))):
                    langs[i] = l

                profiles_list.append({"git_id": profile.id,"login": profile.login, "name": profile.name,
                    "email": profile.email, "location": profile.location, "date_added": timezone.now(),
                    "organization": profile.company, "avatar_url": profile.avatar_url, "html_url": profile.html_url,
                    "language_1": langs[0], "language_2": langs[1], "language_3": langs[2], "accept": True})

            formset = ProfileFormset(initial = profiles_list)

            return render(request, 'gitprofiles/select_profile.html', {'formset': formset})

    else:
        form = SearchForm()

    return render(request, 'gitprofiles/search.html', {'form': form})


def save_profiles(request):
    # if this is a POST request we need to process the form data
    ProfileFormset = formset_factory(ProfileForms,  extra=0)

    if request.method == 'POST':
        formset = ProfileFormset(request.POST)
        # check whether it's valid:
        for key, value in request.POST.items():
            print(key, value)

        print("Check if form is valid")

        if formset.is_valid():

            print("preparing to save", len(formset), "profiles")
            for form in formset:
                cd = form.cleaned_data
                a = Profiles( git_id = cd.get('git_id'), login= cd.get('login'),
                    name = cd.get('name'), email = cd.get('email'),
                    location = cd.get('location'), date_added = timezone.now(),
                    organization= cd.get('organization'), avatar_url = cd.get('avatar_url'),
                    language_1 = cd.get('language_1'), language_2 = cd.get('language_2'),
                    language_3 = cd.get('language_3'), github_url = cd.get('html_url'))


                if cd.get('accept') == True:
                    print("Git login:", cd.get('login'), end="")
                    try:
                        a.save()
                        print(" saved!")
                    except Exception as e:
                        print(" ERROR!")
                        print("--------------------------")
                        print(e)
                        print(cd)
                        print("--------------------------")

            return HttpResponse('Saved!')
        else:
            print("form is invalid")
            print(formset.errors)
            for key, value in request.POST.items():
                print(key, value)

    else:
        print("Request method is",request.method)

    return HttpResponse('FAILED!')
