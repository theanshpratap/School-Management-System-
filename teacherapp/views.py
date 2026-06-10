from django.shortcuts import render, redirect
from adminapp.models import Teacher, Student, Attendance
from django.core.files.storage import FileSystemStorage
from . models import StudyMaterial
import datetime
# Create your views here.

# teacher home view----------------------------------------------------------------------------
def teacherhome(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            # tsalary=Teacher.objects.all() optianl hai
            st=Student.objects.filter(sclass=teacher.tclass).count()
            std=Student.objects.filter(sclass=teacher.tclass)
            At=Attendance.objects.filter(status="P",sclass=teacher.tclass,created_date=datetime.date.today()).count()
            Ab=Attendance.objects.filter(status="A",sclass=teacher.tclass,created_date=datetime.date.today()).count()
            sl=StudyMaterial.objects.filter(tclass=teacher.tclass).count()
            return render(req,'teacherhome.html',{'teacher':teacher,'st':st,'std':std,'At':At,'Ab':Ab,'sl':sl})
    except KeyError:
        return redirect('login')



# teacher profile view---------------------------------------------------------------------------
def teacherprofile(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                address=req.POST['address']
                qualification=req.POST['qualification']
                Teacher.objects.filter(emailaddress=teacherid).update(name=name,fname=fname,mname=mname, gender=gender,dob=dob,contactno=contactno,address=address,qualification=qualification)
                return redirect('teacherapp:teacherprofile')
            return render(req,'teacherprofile.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')


def uploadpic(req):
    if req.method=="POST":
        teacherid=req.session['teacherid']
        teacher=Teacher.objects.get(emailaddress=teacherid)
        pic=req.FILES['pic']
        fs=FileSystemStorage()
        filename=fs.save(pic.name,pic)
        teacher.pic=filename
        teacher.save()
        return redirect('teacherapp:teacherprofile')
   
        
def tchangepass(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                oldpassword=req.POST['oldpassword']
                newpassword=req.POST['newpassword']
                cnfpassword=req.POST['cnfpassword']
                if newpassword!=cnfpassword:
                    msg="Please enter correct password"
                    return render(req,'tcahngepassword.html',{'msg':msg})
                elif teacher.password!=oldpassword:
                    msg="Wrong Password"
                    return render('tchangepassword.html',{'msg':msg})
                elif teacher.password==oldpassword:
                    Teacher.objects.filter(emailaddress=teacherid).update(password=newpassword)
                    return redirect('teacherapp:teacherlogout')
            return render(req,'tchangepass.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')


# teacher logout view-------------------------------------------------------------
def teacherlogout(req):
    try:
        if req.session['teacher']!=None:
            del req.session['teacherid']
            return redirect('login')
    except KeyError:
        return redirect('login')


# Attendance view------------------------------------------------------
def addattend(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            st=Student.objects.filter(sclass=teacher.tclass)
            if req.method=="POST":
                sid=req.POST['sid']
                name=req.POST['name']
                rollno=req.POST['rollno']
                status=req.POST['status']
                created_date=req.POST['created_date']
                a=Attendance.objects.filter(sid=sid,created_date=created_date).first()
                if a is not None:
                    msg="Already Marked Attendance for this Student"
                    return render(req,'addattend.html',{'msg':msg,'st':st,'teacher':teacher})
                else:
                    att=Attendance(sid=sid, name=name, rollno=rollno,sclass=teacher.tclass,tclass=teacher.tclass,status=status, created_date=created_date)
                    att.save()
                    return redirect('teacherapp:addattend')
            return render(req,'addattend.html',{'teacher':teacher,'st':st})
    except KeyError:
        return redirect('login')


# view Attendance view------------------------------------------------------
def viewattend(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            att=Attendance.objects.filter(sclass=teacher.tclass)
            return render(req,'viewattend.html',{'teacher':teacher,'att':att})
    except KeyError:
        return redirect('login')


# study material view------------------------------------------------------------------------
def addslm(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                title=req.POST['title']
                sm=req.FILES['sm']
                slm=StudyMaterial(title=title, sm=sm, tclass=teacher.tclass)
                slm.save()
                return redirect('teacherapp:viewslm')
            return render(req,'addslm.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')


#  view study material view------------------------------------------------------------------------
def viewslm(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            slm=StudyMaterial.objects.all()
            return render(req,'viewslm.html',{'teacher':teacher,'slm':slm})
    except KeyError:
        return redirect('login')

