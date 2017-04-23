# Git Profiles Miner

This is a simple tool to look up for hireable developers using git search engine.

# How to setup everything
Create a settings.ini inside gitMiner folder (where settings.py is located) and populate it:

```
[settings]
SECRET_KEY='your very secret key goes here'
DEBUG=TrueOrFalse
USERNAME=yourgithub@email.com
PASSWORD=yourGithubPassword
```
now you just do as you would with a django-project, migrate everything, create the superuser and runserver
