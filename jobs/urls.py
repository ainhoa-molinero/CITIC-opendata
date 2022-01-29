from django.urls import path, include
from . import views


urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:job_id>', views.detail, name='detail'),
    path('edit/<str:id_archivo>', views.edit_form, name='edit_form'),
]
