from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=156)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    duration = models.CharField(max_length=155)
    location = models.CharField(max_length=156)
    image = models.ImageField(upload_to='posts/')
    def __str__(self):
        return f"{self.title} - {self.date} - {self.duration}"
