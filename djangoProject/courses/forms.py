from django import forms
from courses.models import Course,Teacher


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'category', 'teacher', 'duration', 'type', 'image']


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'category', 'teacher', 'duration', 'type', 'image']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age', 'degree', 'email', 'image',]