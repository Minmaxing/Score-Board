"""
Config of the admin screen.
Made by Mark Dzoljic
"""

from django.contrib import admin
from .models import Student, Team, PointEntry

# Creates classes for admin screen
class TeamAdmin(admin.ModelAdmin):
    """Admindisplay for Team class"""
    list_display = ['name', 'thumbnail', 'points']

class UserAdmin(admin.ModelAdmin):
    """Admindisplay for User class"""
    fields = ('username', 'password', 'name', 'subject')
    list_display = ['username', 'name', 'subject', 'given_points']

class StudentAdmin(admin.ModelAdmin):
    """Admindisplay for Student class"""
    list_display = ['name', 'OG_name', 'team', 'points']
    list_filter = ['team']

class PointEntryAdmin(admin.ModelAdmin):
    """Admindisplay for PointEntry class"""
    list_display = ['teacher', 'student', 'points', 'team', 'date']
    list_filter = ['teacher', 'student']

# Register your models here.
#admin.site.register(User, UserAdmin)
admin.site.register(PointEntry, PointEntryAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Team, TeamAdmin)
