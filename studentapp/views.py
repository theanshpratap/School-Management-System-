from django.shortcuts import render,redirect
from adminapp.models import Student, Attendance
from django.core.files.storage import FileSystemStorage
from teacherapp.models import StudyMaterial
import datetime
# Create your views here.

# student view-----------------------------------------------------------------------
def studenthome(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            At=Attendance.objects.filter(status="P",tclass=student.sclass,created_date=datetime.date.today()).count()
            Ab=Attendance.objects.filter(status="A",tclass=student.sclass,created_date=datetime.date.today()).count()
            smt=StudyMaterial.objects.filter(tclass=student.sclass).count()
            return render(req,'studenthome.html',{'student':student,'smt':smt,'At':At,'Ab':Ab})
    except KeyError:
        return redirect('login')



# student profile view-----------------------------------------------------------------------
def studentprofile(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            if req.method=="POST":
                rollno=req.POST['rollno']
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                altrnum=req.POST['altrnum']
                address=req.POST['address']
                emailaddress=req.POST['emailaddress']
                sclass=req.POST['sclass']
                feepaid=req.POST['feepaid']
                duefees=req.POST['duefees']
                Student.objects.filter(emailaddress=studentid).update(rollno=rollno, name=name, fname=fname,mname=mname, gender=gender,dob=dob, contactno=contactno, altrnum=altrnum,address=address, sclass=sclass, feepaid=feepaid, duefees=duefees)
                return redirect('studentapp:studentprofile')
            return render(req,'studentprofile.html',{'student':student})
    except KeyError:
        return redirect('login')

#student upload pic ---------------------------------------------------
def uploadpic(req):
    if req.method=="POST":
        studentid=req.session['studentid']
        student=Student.objects.get(emailaddress=studentid)
        pic=req.FILES['pic']
        fs=FileSystemStorage()
        filename=fs.save(pic.name,pic)
        student.pic=filename
        student.save()
        return redirect('studentapp:studentprofile')


# student change password------------------------------------------------
def schangepass(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            if req.method=="POST":
                oldpassword=req.POST['oldpassword']
                newpassword=req.POST['newpassword']
                cnfpassword=req.POST['cnfpassword']
                if newpassword!=cnfpassword:
                    msg="Please enter correct password"
                    return render(req,'scahngepassword.html',{'msg':msg})
                elif student.password!=oldpassword:
                    msg="Wrong Password"
                    return render('schangepassword.html',{'msg':msg})
                elif student.password==oldpassword:
                    Student.objects.filter(emailaddress=studentid).update(password=newpassword)
                    return redirect('studentapp:studentlogout')
            return render(req,'schangepass.html',{'student':student})
    except KeyError:
        return redirect('login')


# student logout view-------------------------------------------------------------
def studentlogout(req):
    try:
        if req.session['student']!=None:
            del req.session['studentid']
            return redirect('login')
    except KeyError:
        return redirect('login')


# student attandance--------------------------------------------------------------------------------
def stuattend(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            att=Attendance.objects.filter(sid=student.id)
            return render(req,'stuattend.html',{'student':student,'att':att})
    except KeyError:
        return redirect('login')



# view slm-----------------------------------------------------------------------
def stuslm(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            slm=StudyMaterial.objects.filter(tclass=student.sclass)
            return render(req,'stuslm.html',{'student':student,'slm':slm})
    except KeyError:
        return redirect('login')
