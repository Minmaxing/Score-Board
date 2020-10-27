"""
This file forms all the different views and renders the templates.
Made by Mark Dzoljic
"""

from django import forms
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout
from score_board.models import Student, Team, PointEntry

# Classes
class LoginForm(forms.Form):
    login = forms.CharField(label="new Login")

# Create your views here.
def index(request, message=""):
    """ Index Page. Displays teams and scores"""
    teams = Team.objects.all()
    return render(request, "score_board/index.html",
                  {"teams": teams, "message": message})

def loginview(request):
    """Creates Login Screen"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate User via Django login system.
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # Confirm credentials are correct.

            auth_login(request, user)
            return render(request, "score_board/points.html")
        else:
            return render(request, "score_board/loginview.html",
                          {"message": "Wrong username/password!"})
    else:
        return render(request, "score_board/loginview.html")

def logoutview(request):
    """Logout route"""
    logout(request)
    return index(request, "Succesfully logged out")

def points(request):
    '''Search Student screen and click button to give points'''

    if request.method == "GET":
        return render(request, "score_board/points.html")

    if request.method == "POST":
        # Get query.
        query = request.POST['search']

        # Send results to user
        students = Student.objects.filter(Q(name__icontains=query) | Q(OG_name__icontains=query))\
                    .values_list(named=True)
        return render(request, "score_board/points.html", {"students": students})

def results(request, student_id):
    """ Ask how many points should be awarded"""
    student = Student.objects.get(id=student_id)
    return render(request, "score_board/results.html", {"student": student})

def finalize(request, student_id):
    """ Finalize the points entry and redirect to index """
    points_num = request.POST.get('points', False)
    student = Student.objects.get(id=student_id)
    user_obj = request.user

    # Create entry.
    entry = PointEntry.objects.create(teacher=user_obj, student=student, points=points_num)
    entry.save()

    # Return user to login screen.
    return index(request, f"{points_num} points given to {student.name}")
