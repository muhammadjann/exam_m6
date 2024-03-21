import datetime
from uuid import uuid4

from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractBaseModel):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"
        db_table = "category"


class Course(AbstractBaseModel):
    TYPE_CHOICE = [
        ('standard', 'Standard'),
        ('bootcamp', 'Bootcamp'),
        ('online', 'Online'),
    ]

    name = models.CharField(max_length=50)
    category = models.ManyToManyField('Category', related_name="subjects")
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name="subjects")
    duration = models.IntegerField()
    image = models.ImageField(upload_to="courses/", null=True, blank=True)
    type = models.CharField(max_length=15, choices=TYPE_CHOICE, default="s")

    def __str__(self):
        return f'{self.name} | {self.type}'

    class Meta:
        verbose_name_plural = "Courses"
        verbose_name = "Course"
        db_table = "course"
        ordering = ["name"]


class Teacher(AbstractBaseModel):
    Degree = [
        ('middle', 'Middle'),
        ('senior', 'Senior'),
        ("master", "Master"),
        ("academic", "Academic"),
    ]

    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    category = models.ManyToManyField('Category', related_name="teacher")
    degree = models.CharField(max_length=9, choices=Degree)
    image = models.ImageField(upload_to="teachers/", null=True)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        db_table = "teacher"

    def __str__(self):
        return "{0}{1}".format(self.first_name, self.last_name)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
