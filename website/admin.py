from django.contrib import admin
from .models import Project, Contact, Settings

admin.site.register(Project)
admin.site.register(Contact)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):

        return False

    def has_delete_permission(self, request, obj=None):

        return False