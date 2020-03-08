from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name="product-home"),
    path('create/',create,name="product-create"),
    path('edit/<int:id>/',edit,name="product-edit"),
    path('delete/<int:id>/',delete,name="product-delete")
]