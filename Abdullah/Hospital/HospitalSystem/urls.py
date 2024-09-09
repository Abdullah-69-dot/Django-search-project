from django.urls import path
from . import views
urlpatterns = [
path("",views.register, name="r"),
    path("home/",views.search_doctors , name='index'),
    path("login",views.login_view, name='login'),
]