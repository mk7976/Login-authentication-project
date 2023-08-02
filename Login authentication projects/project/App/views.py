from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# Create your views here.
def Loginpage(request):
    return render(request, 'login.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['w1']
        password = request.POST['w2']
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is None:
            a = "Username Or Password is Wrong"
            return render(request, 'login.html', {'msg': a})
        if user is not None:
            login(request, user)
            a = username
            # return redirect('Home')
            return render(request, 'home.html', {'a1': a})

    # else:
    # Return an 'invalid login' error message.
    # a = "You Are Not Ragistered Till Now"
    # return render(request, 'login.html', {'msg': a})


def Home(request):
    return render(request, 'home.html')


def Logout(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'login.html')

# userid -mk123
# password=1234.
