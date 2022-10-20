from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Course, Lesson

# Create your views here.

def hello(request):

    return HttpResponse('hello')

def index(request):
    # Return list of courses
    queryset = Course.objects.all()

    context = {
        'courses': queryset
    }

    return render(request, 'courses/index.html', context)


def course_detail(request, course_slug):
    # Send course, then lesson set
    course = Course.objects.get(slug=course_slug)
    lesson_set = course.lesson_set.all()

    context = {
        'course': course,
        'lessons': list(lesson_set)
    }

    return render(request, 'courses/course_detail.html', context)
    
def lesson_detail(request, course_slug, lesson_slug):

    lesson = Lesson.objects.select_related('course').get(slug=lesson_slug)

    context = {
        'lesson': lesson
    }

    return render(request, 'courses/lesson_detail.html', context)