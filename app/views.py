from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail

def registration(request):
    ufo=userform()
    pfo=profileform()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=userform(request.POST)
        pfd=profileform(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            nsud=ufd.save(commit=False)
            
            password=ufd.cleaned_data['password']
            nsud.set_password(password)
            
            nsud.save()

            nspd=pfd.save(commit=False)
            nspd.username=nsud
            nspd.save()

            send_mail('loginform',
                      'registration is success',
                      'asifazeem520@gmail.com',
                      [nsud.email],
                      fail_silently=True)
            return HttpResponse('registation successfully completed')
        else:
            return HttpResponse('is not valid')
    return render(request,'registration.html',d)