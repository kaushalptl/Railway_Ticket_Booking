from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from login_module.models import *
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from django.core.mail import send_mail
from django.conf import settings
import smtplib
def login(request):
    return render(request, 'login.html')


def adminlogin(request):
    return render(request, 'adminlogin.html')

def verification(request):
    id1 = request.POST.get('id')
    passwd = request.POST.get('password')
    id2=int(id1)
    print(id1)
    print(passwd)
    user_list = Person.objects.all()
    for user in user_list:
        print(user.id)
        if user.id == id2 and user.password == passwd:
            request.session['id'] = user.id
            trains =Trainlist.objects.all()
            if id2 == 26799:
                return render(request, "adminhome.html", )
            else:
                return render(request,"loggedin.html",{'trains':trains})

    context = {'error_msg': "E-mail or Password is Incorrect", }
    return render(request, 'loginfailed.html', context)


def adminhome(request):
    return render(request, 'adminhome.html')

def valid(request):
    return render(request, 'loggedin.html')

def addtrainpage(request):
    return render(request, 'addtrain.html')

def removetrainpage(request):
    return render(request, 'removetrain.html')

def invalid(request):
    return render(request, 'loginfailed.html')


def again(request):
    return render(request, 'login.html')

def trainadded(request):
    return render(request, 'trainadded.html')


def trainremoved(request):
    return render(request, 'trainremoved.html')

def home(request):
    return render(request, 'homepage.html')

def ticket(request):
    c = {}
    c.update(csrf(request))
    train1 = request.POST.get('train')
    date1 = request.POST.get('date')
    src1 = request.POST.get('source')
    dest1 = request.POST.get('destination')
    n1 = request.POST.get('number')
    n2=int(n1)
    mail1 = request.POST.get('email')
    s1=cost.objects.get(station = src1)
    s2=cost.objects.get(station = dest1)
    far=int(s1.costy)-int(s2.costy)
    if far<0:  
        far=0-far
    fare=(far*n2)
    m_list =[]
    m_list.append(mail1)
    content = "Dear Customer,\n           Your Ticket is Confirmed! \n Your train is:" + train1 + "\n date :  " + date1 + "\n Hope In at:  " + src1 + "\n Destinatiton :" + dest1 + "\n Number of Tickets :" + n1 + "\n Total Cost : " + str(fare) + "\n \n \n Thank You For Choosing BOOKING EXPRESS. \n  Wish you Happy Journey!"
    subject = "Express Booking"
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject,content,email_from,m_list)
    dt = ticketdetails(tnm=train1, dt=date1,src=src1, dest=dest1, num=n1, mail=mail1,cost=fare)
    dt.save()
    return render(request, 'ticket.html', {'cost':fare,'train': train1, 'date': date1, 'source':src1, 'destination':dest1, 'number':n1,'email':mail1})

def addtrain(request):
    c = {}
    c.update(csrf(request))
    tid1 = request.POST.get('trainid')
    tname1 = request.POST.get('trainname')
    t = Trainlist(tid=tid1, tname=tname1)
    t.save()
    return HttpResponseRedirect('/login_module/trainadded/')


def remove(request):
    co=Trainlist.objects.get(tid=request.POST.get('trainid'))
    co.delete()
    return HttpResponseRedirect('/login_module/trainremoved/')



