from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path("delete/<int:id>", views.delete_contact, name="delete_contact"),
    path("update/<int:id>", views.update_contact, name="update_contact"),
]
