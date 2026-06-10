from django.urls import path
from . import views

urlpatterns=[
    path('studenthome/',views.studenthome,name='studenthome'),
    path('studentprofile/',views.studentprofile,name='studentprofile'),
    path('uploadpic/',views.uploadpic,name='uploadpic'),
    path('schangepass/',views.schangepass,name='schangepass'),
    path('studentlogout/',views.studentlogout,name='studentlogout'),
    path('stuattend/',views.stuattend,name='stuattend'),
    path('stuslm/',views.stuslm,name='stuslm'),
    
]