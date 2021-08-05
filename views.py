from django.shortcuts import render
from .models import Contact,Register,Male,Female


# from .models import Contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        firstname_f = request.POST.get('firstname')
        lastname_f = request.POST.get('lastname')
        email_f = request.POST.get('email')
        gender_f = request.POST.get('gender')
        r = Register(firstname=firstname_f, lastname=lastname_f, email=email_f, gender=gender_f)
        r.save()
        if request.POST.get('gender') == 'Male':
            return render(request,'myapp/male.html')
        else:
            return render(request, 'myapp/female.html')
    else:
        return render(request,'myapp/index.html')

    # if value of gender == Male then request render to male.html else render to Female.html
        # else render req to RegistrationFailed.html.



def about(request):
    return render(request, 'myapp/about.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()
        return render(request, 'myapp/thank.html')
    else:
        return render(request, 'myapp/contact.html')


def thank(request):
    return render(request, 'myapp/thank.html')
def failed(request):
    return render(request, 'myapp/failed.html')

def male(request):
    if request.method == 'POST':
        age_a = request.POST.get('age')
        m = Male(age=age_a)
        m.save()
        if request.POST.get('age') == '18-35':
            return render(request, 'myapp/m18-35.html')
        if request.POST.get('age') == '36-55':
            return render(request, 'myapp/m36-55.html')
        if request.POST.get('age') == 'More than 55':
            return render(request, 'myapp/mmorethan55.html')
    else:
        return render(request, 'myapp/index.html')

#if value == 18-35 req render to m18-35
#if value == 36-55 req render to m36-55
#if value == morethan55 req render to mmorethan55

def female(request):
    if request.method == 'POST':
        age_a = request.POST.get('age')
        f = Female(age=age_a)
        f.save()
        if request.POST.get('age') == '18-35':
            return render(request, 'myapp/f18-35.html')
        if request.POST.get('age') == '36-55':
            return render(request, 'myapp/f36-55.html')
        if request.POST.get('age') == 'More than 55':
            return render(request, 'myapp/fmorethan55.html')
    else:
        return render(request, 'myapp/index.html')

    # if value == 18-35 req render to f18-35
    # if value == 36-55 req render to f36-55
    # if value == morethan55 req render to fmorethan55