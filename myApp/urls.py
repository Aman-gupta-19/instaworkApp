from django.urls import path
from . import views

urlpatterns = [
    path('ListPage/',views.ListPage, name = 'ListPage'),
    path('AddPage/',views.AddPage, name = 'AddPage'),
    path('EditPage/',views.EditPage, name = 'EditPage'),
    path('DelRec/',views.DelRec, name = 'DelRec')
]