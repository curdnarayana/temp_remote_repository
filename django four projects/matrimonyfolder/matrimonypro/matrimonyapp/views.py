from django.shortcuts import render,redirect,HttpResponse
from .models import MatrimonyData
from .forms import RegistrationForm,LoginForm, PasswordForm
# from django.http.response import HttpResponse
import  datetime

def loginview(request):

    if request.method =='POST':
        lform = LoginForm(request.POST)

        if lform.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = MatrimonyData.objects.filter(username=username)
            pwd = MatrimonyData.objects.filter(password2=password)
            if user and pwd:
                return redirect('/#/')
            else:
                return redirect('/home/')
    else:
        lform = LoginForm()
        return render(request,'login_matri_backup.html',{'lform':lform})

def registrationview(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            father_name = form.cleaned_data.get('father_name')
            mother_name = form.cleaned_data.get('mother_name')
            sal = form.cleaned_data.get('sal')
            mobile = form.cleaned_data.get('mobile')
            color = form.cleaned_data.get('color')
            weight = form.cleaned_data.get('weight')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            dob = form.cleaned_data.get('dob')
            height = form.cleaned_data.get('height')
            gender = form.cleaned_data.get('gender')
            preffered_location = form.cleaned_data.get('preffered_location')
            jobtype = form.cleaned_data.get('jobtype')
            looking_for = form.cleaned_data.get('looking_for')
            address = form.cleaned_data.get('address')

            m = MatrimonyData(
                first_name=first_name,
                last_name=last_name,
                father_name=father_name,
                mother_name=mother_name,
                sal=sal,
                mobile=mobile,
                color=color,
                weight=weight,
                email=email,
                username=username,
                password1=password1,
                password2=password2,
                dob=dob,
                height=height,
                gender=gender,
                jobtype=jobtype,
                looking_for=looking_for,
                address=address,
                locations=preffered_location

            )
            m.save()
            form = RegistrationForm()
            return render(request, 'matri_reg.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'matri_reg.html', {'form':form})

def password(request):
    if request.method == "GET":
        pform = PasswordForm()
        return render(request, 'password1.html', {'pform': pform})
    else:
        response = HttpResponse()
        form = PasswordForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']
            try:
                x = MatrimonyData.objects.filter(username=uname)
                if pass1 == pass2:
                    x.update(password1 = pass1)
                    x.update(password2 = pass2)

                    return render(request, 'passwordlog1.html')
                else:
                    return HttpResponse("Passwords Didn't match")
            except MatrimonyData.DoesNotExist:
                return HttpResponse("Username Not Found ")

        else:
            return HttpResponse('Invalid form')
            # print(forms.errors)


def home(request):
    return render(request,'matri_home1.html')


def services(request):
    return render(request,'matri_services1.html')


def clients(request):
    return render(request,'matri_clients1.html')


def boys(request):
    boys_data = MatrimonyData.objects.filter(gender='M')
    return render(request,'matri_boys1.html',{'boys':boys_data})

def girls(request):
    girls_data = MatrimonyData.objects.filter(gender='F')
    return render(request,'matri_girls1.html',{'girls':girls_data})

def gallery(request):
    return render(request,'matri_gallery.html')


def feedback(request):
    return render(request,'matri_feedback.html')

def team(request):
    return render(request,'matri_team.html')