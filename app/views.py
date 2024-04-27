from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from app.forms import SignUpForm, LoginForm, ChangePassForm, EditProfileForm



def user_sign_up_view(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "User has been Registered Successfullty !!!")
            return redirect("login")
    else:
        fm = SignUpForm()
    return render(request, "signup.html", {"form":fm})


def user_login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User has been Logged In Successfully !!!")
                    return redirect("profile")
        else:
            fm = LoginForm()
        return render(request, "login.html", {"form":fm})
    else:
        return redirect("profile")


def user_profile_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, "User Profile has been Updated")
                fm.save()
        else:
            fm = EditProfileForm(instance=request.user)
        return render(request, "profile.html", {"user":request.user, "form":fm})
    else:
        return redirect("login")

def user_logout_view(request):
    if request.user.is_authenticated:   
        logout(request)
        messages.success(request, "User Logged Out Successfully !!!")
        return redirect("login")
    else:
        return redirect("login")


def user_password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = ChangePassForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Password has been Changed !!!")
                update_session_auth_hash(request, fm.user)
                return redirect('profile')
        else:
            fm = ChangePassForm(user=request.user)
        return render(request, "passchange.html", {"form":fm})
    else:
        return redirect("login")