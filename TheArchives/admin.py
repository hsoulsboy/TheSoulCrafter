from django.contrib import admin

from .models import Character, Personality, Origin

admin.site.register([Character, Personality, Origin])