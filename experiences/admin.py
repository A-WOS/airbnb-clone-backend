from django.contrib import admin

from experiences.models import Experience, Perk


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):
    pass
