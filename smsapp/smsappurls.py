from django.urls import path
from . views import *

urlpatterns=[
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('logcode/',logcode,name='logcode'),
    path('fdsmsg/',fdsmsg,name='fdsmsg'),
    path('visandmis/',visandmis,name='visandmis'),
    path('chairman/',chairman,name='chairman'),
    path('principal/',principal,name='principal'),
    path('smteam/',smteam,name='smteam'),
    path('newsevent/',newsevent,name='newsevent'),
    path('academic/',academic,name='academic'),
    path('addmission/',addmission,name='addmission'),
    path('fstructure/',fstructure,name='fstructure'),
    path('transport/',transport,name='transport'),
    path('smartclass/',smartclass,name='smartclass'),
    path('medicalroom/',medicalroom,name='medicalroom'),
    path('rules/',rules,name='rules'),
    path('otherfacilities/',otherfacilities,name='otherfacilities'),
    path('career/',career,name='career'),
    path('video/',video,name='video'),

]