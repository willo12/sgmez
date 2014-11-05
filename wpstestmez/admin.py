from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import DocPage

admin.site.register(DocPage, PageAdmin)