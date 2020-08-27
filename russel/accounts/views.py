from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def logout(request):

    auth.logout(request)
    return redirect("accounts:login")
    # return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect("travello:home")
            # return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("accounts:login")

    else:
        return render(request,'accounts/login.html')


def register(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				messages.success(request, 'Account was created for ' + username)

				return redirect('accounts:login')


		context = {'form':form}
		return render(request, 'accounts/register.html', context)



    # if request.method =='POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     email = request.POST['email']
    #
    #     if password1 == password2:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request,'Username Taken')
    #             return redirect('register')
    #         elif User.objects.filter(email=email).exists():
    #             messages.info(request,'Email Taken')
    #             return redirect('register')
    #         else:
    #             user = User.objects.create_user(username = username,
    #             password = password1,
    #             email = email,
    #             first_name = first_name,
    #             last_name = last_name)
    #             user.save();
    #             print('user created')
    #             return redirect('login')
    #     else:
    #         print("Password Do not match...")
    #         return redirect('register')
    #     return redirect('/')
    #
    # else:
    #     return render(request,'register.html')
