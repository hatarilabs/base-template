from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import Project, SuscriptorType, SuscriptionRecords

class UserAdmin(admin.ModelAdmin):
	#search_fields = ['first_name']
	raw_id_fields = ['user']

class ProjectAdmin(admin.ModelAdmin):
	#search_fields = ['first_name']
	model = Project
	list_display = ['modelName','user','token']

admin.site.register(Session)
#admin.site.register(Project)
admin.site.register(SuscriptorType)
admin.site.register(SuscriptionRecords,UserAdmin)
admin.site.register(Project,ProjectAdmin)
