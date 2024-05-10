"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movieapp import views
app_name="movieapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name="home"),
    path('',views.HomeView.as_view(),name="home"),
    # path('detail/<int:n>/',views.detail,name="detail"),
    path('detail/<int:pk>/',views.Detail.as_view(),name="detail"),
    # path('update/<int:n>/',views.update,name="update"),
    path('update/<int:pk>/',views.Update.as_view(),name="update"),
    # path('delete/<int:n>/',views.delete,name="delete"),
    path('delete/<int:pk>/',views.Delete.as_view(),name="delete"),
    # path('addmovie/',views.addmovie,name="addmovie"),
    path('addmovie/',views.AddMovie.as_view(),name="addmovie"),
]

