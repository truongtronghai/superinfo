from django.contrib import admin
from .models import Option


class OptionAdmin(admin.ModelAdmin):
    list_display = ("name", "value")


# Register your models here.
admin.site.register(Option, OptionAdmin)
