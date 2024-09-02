from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("index",views.index,name="home"),
    path("about",views.about,name="index"),
    path("service",views.service,name="index"),
    path("contact",views.contact,name="index"),
    path("feature",views.feature,name="index"),
    path("appointment",views.appointment,name="index"),
    path("team",views.team,name="index"),
    path("testimonial",views.testimonial,name="index"),
    path("err",views.err,name="index"),
]