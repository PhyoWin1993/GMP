
from django.urls import path
from .views import *

urlpatterns = [
    path('',create_all,name='cat-all'),
    path('create/',create,name='cat-create'),
    path('edit/',edit,name='cat-edit')
]
