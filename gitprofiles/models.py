from django.db import models
from django.utils import timezone

class Profiles(models.Model):
    git_id = models.IntegerField(unique=True)
    login = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    date_added = models.DateTimeField('date added')
    organization = models.CharField(max_length=200, blank=True, null=True)
    blog_url = models.CharField(max_length=200, blank=True, null=True)
    github_url = models.CharField(max_length=200, blank=True, null=True)
    avatar_url = models.CharField(max_length=200, blank=True, null=True)
    resume_url = models.CharField(max_length=200, blank=True, null=True)
    portifolio_url = models.CharField(max_length=200, blank=True, null=True)
    linkedin_url = models.CharField(max_length=200, blank=True, null=True)
    stack_url = models.CharField(max_length=200, blank=True, null=True)
    language_1= models.CharField(max_length=100, blank=True, null=True)
    language_2= models.CharField(max_length=100, blank=True, null=True)
    language_3= models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "ID: [{}] NAME:[{}]".format(self.git_id, self.name)

    def was_added_recently(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=60)
