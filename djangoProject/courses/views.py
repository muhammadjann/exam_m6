from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Course, Category
from .forms import CourseCreateForm, EditCourseForm, TeacherForm
from django.http import HttpResponseServerError



def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/cources.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def course_create(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses:courses')
    else:
        form = CourseCreateForm()
    return render(request, 'courses/form.html', {'form': form, 'title': 'Course Creation'})


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = EditCourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:courses')
    else:
        form = EditCourseForm(instance=course)
        return render(request, 'courses/form.html', {'form': form, 'title': 'Edit'})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk,)
    course.delete()

    return redirect('courses:courses')


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'courses/teacher_detail.html', {'teacher':teacher})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm()
        return render(request, 'courses/form.html', {'form': form, 'title': 'Teacher Creation'})


def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm(instance=teacher)
        return render(request, 'courses/form.html', {'form': form, 'title': 'Edit'})


def teacher_delete(request, pk):
    course = get_object_or_404(Teacher, pk=pk,)
    course.delete()

    return redirect('index')
