from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<key>/Values/', views.val, name='Values'),

]