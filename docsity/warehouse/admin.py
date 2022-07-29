from django.contrib import admin

from warehouse.models import University, Faculty, Course, EducationalYear, Professor, Content


@admin.register(University)
class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'city']


@admin.register(Faculty)
class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Course)
class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(EducationalYear)
class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = ['year']


@admin.register(Professor)
class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = ['name', 'family_name', 'title', 'birthday_year']


@admin.register(Content)
class SwapTransactionAdmin(admin.ModelAdmin):
    list_display = ['university', 'faculty', 'course', 'year', 'file']


