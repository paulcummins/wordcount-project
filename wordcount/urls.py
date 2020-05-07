

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dissection/', views.count, name='diss'),
    path('about/', views.about)




]
