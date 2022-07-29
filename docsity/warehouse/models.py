from django.db import models
from model_utils.models import TimeStampedModel


class University(TimeStampedModel):
    name = models.CharField(max_length=511)
    logo = models.ImageField()
    city = models.CharField(max_length=127)


class Faculty(TimeStampedModel):
    name = models.CharField(max_length=127)


class Course(TimeStampedModel):
    title = models.CharField(max_length=127)
    # faculty = models.ForeignKey(on_delete=models.SET_NULL)


class EducationalYear(TimeStampedModel):
    year = models.IntegerField()


class Professor(TimeStampedModel):
    name = models.CharField(max_length=127)
    family_name = models.CharField(max_length=127)
    title = models.CharField(max_length=63)
    birthday_year = models.IntegerField(null=True, blank=True)


class Content(TimeStampedModel):
    university = models.ForeignKey(to=University, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.SET_NULL)
    course = models.ForeignKey(to=Course, on_delete=models.SET_NULL)
    year = models.ForeignKey(to=EducationalYear, on_delete=models.SET_NULL)


class File(TimeStampedModel):
    name = models.CharField(max_length=63)
    file = models.FileField()

# Create your models here.
