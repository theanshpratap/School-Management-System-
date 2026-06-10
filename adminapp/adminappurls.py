from django.urls import path
from . import views

urlpatterns=[
    path('admin/',views.adminhome,name='adminhome'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('addclass/',views.addclass,name='addclass'),
    path('viewclass/',views.viewclass,name='viewclass'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('addsubject/',views.addsubject,name='addsubject'),
    path('viewsubject/',views.viewsubject,name='viewsubject'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('editclass/<id>',views.editclass,name='editclass'),
    path('editsubject/<id>',views.editsubject,name='editsubject'),
    path('editteacher/<id>',views.editteacher,name='editteacher'),
    path('addteacher/',views.addteacher,name='addteacher'),
    path('viewteacher/',views.viewteacher,name='viewteacher'),
    path('delcl/<id>',views.delcl,name='delcl'),
    path('delsub/<id>',views.delsub,name='delsub'),
    path('delteacher/<id>',views.delteacher,name='delteacher'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('editstudent/<id>',views.editstudent,name='editstudent'),
    path('delst/<id>',views.delst,name='delst'),
    path('addnoti/',views.addnoti,name='addnoti'),
    path('viewnoti/',views.viewnoti,name='viewnoti'),

]