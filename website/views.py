from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from website.models import Contact 

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if len(name)<2 or len(email)<8 :
            messages.error(request,"Fill Correctly")
        else:
            ex=Contact(name=name,email=email,subject=subject,message=message)
            ex.save()
            messages.success(request," Send Successfully , Thank You ")
    return render(request,'index.html')
