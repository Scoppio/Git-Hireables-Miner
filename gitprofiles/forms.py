from django import forms

class SearchForm(forms.Form):
	location = forms.CharField(label="Location", max_length=200)
	language = forms.CharField(label="Language", max_length=200)
	repos = forms.CharField(label="Number of Repos", max_length=3)
	followers = forms.CharField(label="Number of followers", max_length=10)

class ProfileForms(forms.Form):
	git_id = forms.IntegerField(required=False)
	login = forms.CharField(max_length=90, required=False)
	avatar_url = forms.CharField(max_length=200, required=False)
	name = forms.CharField(max_length=200, required=False)
	email = forms.CharField(max_length=200, required=False)
	company = forms.CharField(max_length=200, required=False)
	html_url = forms.CharField(max_length=200, required=False)
	blog_url = forms.CharField(max_length=300, required=False)
	date_added = forms.DateField(required=False)
	location = forms.CharField(max_length=200, required=False)
	language_1 = forms.CharField(max_length=100, required=False)
	language_2 = forms.CharField(max_length=100, required=False)
	language_3 = forms.CharField(max_length=100, required=False)
	accept = forms.BooleanField(required=False)

