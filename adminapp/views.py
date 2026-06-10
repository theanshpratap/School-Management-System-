from django.shortcuts import render, redirect
from smsapp.models import Enquiry
from django.utils import timezone
from . models import *
from django.views.decorators.cache import cache_control
import datetime

# Create your views here.
# admin home view---------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def adminhome(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            stu_count=Student.objects.all().count()
            teach_count=Teacher.objects.all().count()
            cls_count=Classes.objects.all().count()
            e_count=Enquiry.objects.all().count()
            am_count=Notification.objects.all().count()
            sb_count=Subject.objects.all().count()
            ps=Attendance.objects.filter(status="P",created_date=datetime.date.today()).count()
            abs=Attendance.objects.filter(status="A",created_date=datetime.date.today()).count()
            context={'adminid':adminid,'stu_count':stu_count,'teach_count':teach_count,'cls_count':cls_count,'e_count':e_count, 'am_count':am_count,'sb_count':sb_count,'ps':ps,'abs':abs}
            return render(req,'adminhome.html',context)
    except KeyError:
        return redirect('login')

# view Enquiry view -----------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def viewenquiry(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            enq=Enquiry.objects.all()
            return render(req,'viewenquiry.html',{'adminid':adminid,'enq':enq})
    except KeyError:
        return redirect('login')

# add class view--------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def addclass(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            if req.method=="POST":
                class_name=req.POST['class_name']
                seats=req.POST['seats']
                roomno=req.POST['roomno']
                created_date=timezone.now()
                cl=Classes(class_name=class_name, seats=seats, roomno=roomno, created_date=created_date)
                cl.save()
                return redirect('adminapp:viewclass')
            return render(req,'addclass.html',{'adminid':adminid})
    except KeyError:
        return redirect('login')

# view class view-------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def viewclass(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            return render(req,'viewclass.html',{'adminid':adminid, 'cl':cl})
    except KeyError:
        return redirect('login')

# admin logout view-------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def adminlogout(req):
    try:
        if req.session['admin']!=None:
            del req.session['adminid']
            return redirect('login')
    except KeyError:
        return redirect('login')

# add subject view---------------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def addsubject(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method == "POST":
                subject_name=req.POST['subject_name']
                sclass=req.POST['sclass']
                steacher=req.POST['steacher']
                book=req.POST['book']
                created_date=timezone.now()
                sub=Subject(subject_name=subject_name, sclass=sclass, book=book, steacher=steacher, created_date=created_date)
                sub.save()
                return redirect('adminapp:viewsubject')
            return render(req,'addsubject.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')

# view subject view---------------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def viewsubject(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            sub=Subject.objects.all()
            return render(req,'viewsubject.html',{'adminid':adminid,'sub':sub})
    except KeyError:
        return redirect('login')

# delete Enquiry view---------------------------------------------------------------------------------------------------------------
def delenq(req,id):
    try:
        if req.session['adminid']!=None:
            Enquiry.objects.get(id=id).delete()
            return redirect('adminapp:viewenquiry')
    except KeyError:
        return redirect('login')


# delete class view----------------------------------------------------------------------------------------------------------------
def delcl(req,id):
    try:
        if req.session['adminid']!=None:
            Classes.objects.get(cid=id).delete()
            return redirect('adminapp:viewclass')
    except KeyError:
        return redirect('login')

# delete subject view---------------------------------------------------------------------------------------------
def delsub(req,id):
    try:
        if req.session['adminid']!=None:
            Subject.objects.get(sid=id).delete()
            return redirect('adminapp:viewsubject')
    except KeyError:
        return redirect('login')



# edit class view----------------------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def editclass(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.get(cid=id)
            if req.method == "POST":
                class_name=req.POST['class_name']
                seats=req.POST['seats']
                roomno=req.POST['roomno']
                Classes.objects.filter(cid=id).update(class_name=class_name,seats=seats,roomno=roomno)
                return redirect('adminapp:viewclass')
            return render(req,'editclass.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')

# edit subject view-----------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def editsubject(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            sub=Subject.objects.get(sid=id)
            if req.method == "POST":
                subject_name=req.POST['subject_name']
                sclass=req.POST['sclass']
                book=req.POST['book']
                steacher=req.POST['steacher']
                Subject.objects.filter(sid=id).update(subject_name=subject_name, sclass=sclass,book=book,steacher=steacher)
                return redirect('adminapp:viewsubject')
            return render(req,'editsubject.html',{'adminid':adminid,'sub':sub})
    except KeyError:
        return redirect('login')

# edit teacher view-----------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def editteacher(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            teacher=Teacher.objects.get(id=id)
            if req.method == "POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                tclass=req.POST['tclass']
                address=req.POST['address']
                salary=req.POST['salary']
                qualification=req.POST['qualification']
                created_date=timezone.now()
                Teacher.objects.filter(id=id).update(name=name, fname=fname, mname=mname, gender=gender, dob=dob, contactno=contactno, emailaddress=emailaddress,tclass=tclass, address=address, salary=salary,qualification=qualification, created_date=created_date)
                return redirect('adminapp:viewteacher')
            return render(req,'editteacher.html',{'adminid':adminid,'teacher':teacher})
    except KeyError:
        return redirect('login')

# add teacher view---------------------------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def addteacher(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                emailaddress=req.POST['emailaddress']
                tclass=req.POST['tclass']
                address=req.POST['address']
                salary=req.POST['salary']
                qualification=req.POST['qualification']
                created_date=timezone.now()
                teacher = Teacher(name=name,fname=fname, mname=mname, gender=gender, dob=dob, contactno=contactno, emailaddress=emailaddress, tclass=tclass, address=address, salary=salary, qualification=qualification, created_date=created_date,password="12345")
                teacher.save()
                return redirect('adminapp:viewteacher')
            return render(req,'addteacher.html',{'adminid':adminid,'cl':cl})
    except KeyError:
        return redirect('login')

# view teacher view-----------------------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def viewteacher(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            teacher=Teacher.objects.all()
            return render(req,'viewteacher.html',{'adminid':adminid,'teacher':teacher})
    except KeyError:
        return redirect('login')

# delete teacher view---------------------------------------------------------------------------------------------
def delteacher(req,id):
    try:
        if req.session['adminid']!=None:
            Teacher.objects.get(id=id).delete()
            return redirect('adminapp:viewteacher')
    except KeyError:
        return redirect('login')

# add student view--------------------------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def addstudent(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            cl=Classes.objects.all()
            if req.method=="POST":
                rollno=req.POST['rollno']
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                altrnum=req.POST['altrnum']
                emailaddress=req.POST['emailaddress']
                sclass=req.POST['sclass']
                address=req.POST['address']
                feepaid=req.POST['feepaid']
                duefees=req.POST['duefees']
                created_date=timezone.now()
                password="12345"
                stu=Student.objects.filter(emailaddress=emailaddress).first()
                if stu is not None:
                    return render(req,'addstudent.html',{'adminid':adminid,'cl':cl,'msg':'This emailaddress is already taken'})
                else:
                    st=Student(rollno=rollno, name=name, fname=fname, mname=mname, gender=gender, dob=dob, contactno=contactno, altrnum=altrnum, emailaddress=emailaddress, sclass=sclass, address=address, feepaid=feepaid, duefees=duefees, created_date=created_date, password=password)
                    st.save()
                    return redirect('adminapp:viewstudent')
            return render(req,'addstudent.html',{'adminid':adminid, 'cl':cl})
    except KeyError:
        return redirect('login')


# view student view--------------------------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def viewstudent(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            st=Student.objects.all()
            return render(req,'viewstudent.html',{'adminid':adminid,'st':st})
    except KeyError:
        return redirect('login')


# edit student view-----------------------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def editstudent(req,id):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            st=Student.objects.get(rollno=id)
            if req.method == "POST":
                rollno=req.POST['rollno']
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                altrnum=req.POST['altrnum']
                emailaddress=req.POST['emailaddress']
                sclass=req.POST['sclass']
                feepaid=req.POST['feepaid']
                duefees=req.POST['duefees']
                address=req.POST['address']
                created_date=timezone.now()
                Student.objects.filter(rollno=id).update(name=name, fname=fname, mname=mname, gender=gender, dob=dob, contactno=contactno, emailaddress=emailaddress,sclass=sclass, address=address,feepaid=feepaid, duefees=duefees, created_date=created_date)
                return redirect('adminapp:viewstudent')
            return render(req,'editstudent.html',{'adminid':adminid,'st':st})
    except KeyError:
        return redirect('login')


# delete studnet view---------------------------------------------------------------------------------------------
def delst(req,id):
    try:
        if req.session['adminid']!=None:
            Student.objects.get(rollno=id).delete()
            return redirect('adminapp:viewstudent')
    except KeyError:
        return redirect('login')


# add notification view -----------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def addnoti(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            if req.method=="POST":
                text=req.POST['text']
                doc=req.FILES['doc']
                created_date=datetime.date.today()
                noti=Notification(text=text,doc=doc,created_date=created_date)
                noti.save()
                return redirect('adminapp:viewnoti')
            return render(req,'addnoti.html',{'adminid':adminid})
    except KeyError:
        return redirect('login')


# add notification view -----------------------------------------------------------------------------------------
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def viewnoti(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            noti=Notification.objects.all()
            return render(req,'viewnoti.html',{'adminid':adminid,'noti':noti})
    except KeyError:
        return redirect('login')



























