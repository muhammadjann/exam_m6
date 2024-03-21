from django.contrib import admin

from courses.models import Category, Course, Teacher


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class CourseAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category__title', 'type')
    list_display = ('name', 'duration', 'teacher', 'type')
    list_filter = ('category', 'type',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter = ("degree",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
