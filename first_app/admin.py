# Register your models here.


from django.contrib import admin
from .models.book import Task, SubTask, Category
from first_app.models import Book
admin.site.register(Book)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date')
    search_fields = ('title', 'description')
    list_filter = ('due_date',)

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'task')
    search_fields = ('title', 'description')
    list_filter = ('due_date', 'task')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)
admin.site.register(Category, CategoryAdmin)


