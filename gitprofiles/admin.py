from django.contrib import admin
from django.db import models
from .ExportCsv import export_as_csv_action
from .models import Profiles

class ProfilesModelAdmin(admin.ModelAdmin):

    actions = [
            export_as_csv_action("CSV Export"),
        ]

    list_display = ["name","email", "location", "date_added", "language_1", "language_2", "language_3"]
    list_filter = ["date_added", "location", "language_1", "language_2", "language_3"]
    search_fields = ["location", "language_1", "language_2", "language_3"]
    
    class Meta:
        model = Profiles

admin.site.register(Profiles, ProfilesModelAdmin)
