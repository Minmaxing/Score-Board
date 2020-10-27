"""
Forms the urls of the app.
Made by Mark Dzoljic
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("loginview/", views.loginview, name='loginview'),
    path("logoutview/", views.logoutview, name='logoutview'),
    path("points/", views.points, name='points'),
    path("results/<int:student_id>", views.results, name='results'),
    path("finalize/<int:student_id>", views.finalize, name='finalize'),
]
