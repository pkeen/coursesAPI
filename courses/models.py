from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # I'd like to add an image to be used to display course in courses list - but havent mastered file uploads in django yet
    # price should probably not be included in this model - I will link it to a product using a store app

    # add draft status so can be worked on without published
    # status options
    STATUS_DRAFT = 'D'
    STATUS_PUBLISHED = 'P'
    STATUS_OPTIONS = [
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISHED, "Published"),
    ]
    status = models.CharField(
        max_length=255, 
        choices=STATUS_OPTIONS, 
        blank = False,
        default=STATUS_DRAFT
        )

    def __str__(self) -> str:
        return self.title
    
    
    class Meta:
        ordering = ['title']

    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # I am considering many-to-many here for multiple lessons being able to be used in multiple courses...
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    text = models.TextField(blank=True)
    # needs a video fieldtype here - perhaps this should just be a link for now??? Or actually server hosted video??
    # video_link = 

    def __str__(self) -> str:
        return self.title

    # For Lesssons will appear on course page in alphabetical order: 
    # I would love to create some kind of drag and drop re-ordering
    # But for now, simply name each lesson with a number 1. 2. etc... (Effective enough)
    class Meta:
        ordering = ['title']

    


