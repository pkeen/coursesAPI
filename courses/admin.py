
from django.contrib import admin
from .models import Course, Lesson
#from django.contrib.admin import ModelAdmin - not needed
from django.db.models.aggregates import Count
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse

# For Course Change Page
class LessonInLine(admin.TabularInline):
    model = Lesson
    fields = ['title', 'edit_lesson']
   # show_change_link: True // NOT WORKING
   
    # for link to full lesson change page
    def edit_lesson(self, lesson):
        url = reverse('admin:courses_lesson_change', args=(lesson.id,) )
        return format_html('<a href="{}">Edit</a>', url)
    
    readonly_fields = ['edit_lesson']
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    # Change Page
    inlines = [LessonInLine]
    prepopulated_fields = { 'slug': ('title', ) }

    
    # Code for changelist page
    # Add lesson count
    list_display = ['title', 'lessons']
    search_fields = ['title__istartswith']

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            lesson_count = Count('lesson')
        )
    @admin.display(ordering='lesson_count')
    def lessons(self, course):
        url = (
            reverse('admin:courses_lesson_changelist') 
            + '?'
            + urlencode({
                'course__id': str(course.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, course.lesson_count )
    
    


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    # Change Page
    prepopulated_fields = { 'slug': ('title', ) }

    # Change List Page
    list_display =[
        'title', 
        'course_link',
        ]
    list_select_related = ['course']    
    list_filter = ['course']
    search_fields = ['title__istartswith']

    
    def course_link(self, lesson):
        url = reverse('admin:courses_course_change', args=(lesson.course.id,) )
        return format_html('<a href="{}">{}</a>', url, lesson.course.title)
    