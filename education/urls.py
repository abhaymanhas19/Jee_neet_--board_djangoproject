from django.contrib import admin
from django.urls import path
from education import views
from django.shortcuts import render, redirect

urlpatterns = [
    path("", lambda request: redirect("/bestneetcoaching")),
    path("<page_id>/", views.home, name="home"),
    path("contact", views.conatacus, name="contact"),
    path("lead", views.userlead, name="lead"),
    path("thankyou",views.thankyoupage,name="thankyoupage")
]
