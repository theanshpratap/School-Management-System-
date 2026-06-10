from django.shortcuts import render, redirect
from . models import Enquiry,AdminLogin
import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminapp.models import Teacher, Student
from adminapp.models import Notification

# Create your views here.
def index(req):
    noti=Notification.objects.all()
    return render(req,"index.html",{'noti':noti})

def about(req):
    return render(req,'about.html')

def visandmis(req):
    return render(req,'visandmis.html')

def chairman(req):
    return render(req,'chairman.html')

def principal(req):
    return render(req,'principal.html')

def smteam(req):
    return render(req,'smteam.html')

def newsevent(req):
    return render(req,'newsevent.html')

def academic(req):
    return render(req,'academic.html')

def fdsmsg(req):
    return render(req,'fdsmsg.html')

def addmission(req):
    return render(req,'addmission.html')

def fstructure(req):
    return render(req,'fstructure.html')

def transport(req):
    return render(req,'transport.html')

def smartclass(req):
    return render(req,'smartclass.html')

def medicalroom(req):
    return render(req,'medicalroom.html')

def rules(req):
    return render(req,'rules.html')

def otherfacilities(req):
    return render(req,'otherfacilities.html')

def career(req):
    return render(req,'career.html')

def video(req):
    return render(req,'video.html')

def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        gender=req.POST['gender']
        address=req.POST['address']
        contactno=req.POST['contactno']
        emailaddress=req.POST['emailaddress']
        enquirytext=req.POST['enquirytext']
        enquirydate=datetime.datetime.today()
        enq=Enquiry(name=name, gender=gender, address=address, contactno=contactno, emailaddress=emailaddress, enquirytext=enquirytext, enquirydate=enquirydate)
        enq.save()
        msg="Your enquiry is submitted successfully"
        return render(req,'contact.html',{'msg':msg})
    return render(req,'contact.html')

def login(req):
    return render(req,'login.html')

def logcode(req):
    if req.method=="POST":
        usertype=req.POST['usertype']
        userid=req.POST['userid']
        password=req.POST['password']
        if usertype=="admin":
            try:
                user=AdminLogin.objects.get(userid=userid,password=password)
                if user is not None:
                    req.session['adminid']=userid
                    return redirect('adminapp:adminhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
        elif usertype=="teacher":
            try:
                teacher=Teacher.objects.get(emailaddress=userid,password=password)
                if teacher is not None:
                    req.session['teacherid']=userid
                    return redirect('teacherapp:teacherhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid user'})
        elif usertype=="student": 
            try:
                student=Student.objects.get(emailaddress=userid, password=password)
                if student is not None:
                    req.session['studentid']=userid
                    return redirect('studentapp:studenthome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid user'})






            

