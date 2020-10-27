"""
Outlines the Database Model
Made by MinMaxing
"""

from django.db import models
from django.conf import settings

# Create your models here.
#class User(AbstractUser):
#    """ User model """
#    name = models.CharField(max_length=64)
#    subject = models.CharField(max_length=64)
""" 
    def given_points(self):
        points = sum(list(PointEntry.objects.filter(teacher=self)\
                     .values_list('points', flat=True)))
        return points

    def __str__(self):
        return f"{self.username}, {self.name}, {self.subject}"
 """
class Team(models.Model):
    """ Team/group model """
    name = models.CharField(max_length=64)
    thumbnail = models.ImageField(upload_to='static/score_board/media/teams')

    def points(self):
        """ Get students and calculate points per team """
        students = list(Student.objects.filter(team=self))
        pointlist = []
        for student in students:
            points = sum(list(PointEntry.objects.filter(student=student).\
                         values_list("points", flat=True)))
            pointlist.append(points)
        return sum(pointlist)

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    """ Student model """
    name = models.CharField(max_length=64)
    OG_name = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.OG_name}"

    def points(self):
        """ Calculate points per student"""
        points = sum(list(PointEntry.objects.filter(student=self)\
                     .values_list('points', flat=True)))
        return points

class PointEntry(models.Model):
    """ Point entry's made by users appointed to a student in a group """
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    points = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def team(self):
        return self.student.team

    def __str__(self):
        return f"{self.teacher} gives {self.points} to {self.student}"
