from django.urls import path

from .views import index, creat, edit, delete

app_name = "api"
urlpatterns = [
    path('', index, name="index"),
    path('creat/', creat, name="creat"),
    path('edit/<int:id>', edit, name="edit"),
    path('delete/<int:id>', delete, name="delete"),
]
