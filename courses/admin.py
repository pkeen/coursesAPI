from django.contrib import admin
from .models import Course, Lesson
#from django.contrib.admin import ModelAdmin - not needed

admin.site.register(Course)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display =['title']
    list_select_related: ['course']

