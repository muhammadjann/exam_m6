from django.shortcuts import render, get_object_or_404, redirect

from .forms import EventForm
from .models import Event


def blogs(request):
    events = Event.objects.all()
    return render(request, 'blog/blog.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'blog/blog_detail.html', {'event': event})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    else:
        form = EventForm()
        return render(request, 'courses/form.html', {'form': form, 'title': ' Event Creation'})


def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk )
    if request.method == 'POST':
        form = EventForm(request, instance=event)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_detail', pk=pk,)

    else:
        form = EventForm(instance=event)
        return render(request, 'courses/form.html', {'form': form, 'title': 'Edit Event'})


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('blog:blog_detail')