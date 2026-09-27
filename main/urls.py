from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentPage, name='studentpage'),
    path('StudentDetails/<int:id>', views.StudentDetails, name='studentdetails')
]
