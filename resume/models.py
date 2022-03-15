from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=255)
    cat_choices = (
        ("programming", "Programming"),
        ("sysadmin","Sysadmin"),
        ("other","Other"),
        ("languages","Languages")
    )
    category = models.CharField(max_length=255, choices=cat_choices)
    proficency = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    def __str__(self):
        return f'{self.name}, {self.category}'
    

class WorkExperiences(models.Model):
    title = models.CharField(max_length=255)
    time_begin = models.DateField(auto_now=False, auto_now_add=False)
    time_end = models.DateField(auto_now=False, auto_now_add=False)
    show_only_years = models.BooleanField(default=False)
    internship = models.BooleanField(default=False)
    current = models.BooleanField(default=False)
    description = models.TextField()
    location = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.title}'
    
class Education(models.Model):
    title = models.CharField(max_length=255)
    time_begin = models.DateField(auto_now=False, auto_now_add=False)
    time_end = models.DateField(auto_now=False, auto_now_add=False)
    show_only_years = models.BooleanField(default=False)
    description = models.TextField()
    finished = models.BooleanField(default=False)
    finished_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.title}'