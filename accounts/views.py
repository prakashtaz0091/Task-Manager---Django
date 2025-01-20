from django.shortcuts import render, redirect
from .forms import StyledUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib import messages



# Custom Login View (optional, you can use the built-in one)
# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'



def login_view(request):
    # print("User created successfully")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password)
        authenticated_user = authenticate(request, username=username, password=password)
        
        if authenticated_user is not None:
            print("authenticated successful")
            login(request, authenticated_user)
            return redirect("home")
        
        messages.error(request, "Invalid username or password")
        return redirect("login_view")
        
        
    
    return render(request, "accounts/login.html")


def signup_view(request):
    
    
    if request.method == "POST":
        filled_form = StyledUserCreationForm(request.POST)
        
        if filled_form.is_valid():
            filled_form.save()
            return redirect('login_view')
        
        context = {
            'form': filled_form
        }
        
        
        return render(request, "accounts/signup.html", context )
        
    
    
    
    signup_form = StyledUserCreationForm()
    
    context = {
        'form': signup_form
    }
    
    
    return render(request, "accounts/signup.html", context )
    
    
