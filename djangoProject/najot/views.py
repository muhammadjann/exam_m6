from django.shortcuts import render
from courses.models import Teacher, Course, Category
from blog.models import Event


def index(request):
    courses = Course.objects.all()[0:3]
    teachers = Teacher.objects.all()[0:3]
    categories = Category.objects.all()
    blogs = Event.objects.all()[0:3]
    return render(request, 'frontpage/index.html', {
        'courses': courses,
        'teachers': teachers,
        'categories': categories,
        'blogs': blogs,
    })


def about(request):
    teachers = Teacher.objects.all()
    return render(request, 'frontpage/about_us.html', {'teachers': teachers})


def contact(request):

    return render(request, 'frontpage/contact_us.html')
