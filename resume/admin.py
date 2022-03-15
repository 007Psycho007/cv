from django.contrib import admin
from .models import Skills, WorkExperiences, Education
# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    list_display = ["title", "time_begin", "time_end"]
    list_filter = ("title",)
admin.site.register(Skills)
admin.site.register(WorkExperiences, WorkAdmin)
admin.site.register(Education)