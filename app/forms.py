from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Set Password", widget=forms.PasswordInput(attrs={"placeholder":"Enter Password", "class":"form-control"}))
    password2 = forms.CharField(label="Confirm Password (again)", widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password", "class":"form-control"}))
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        labels = {"email":"Email ID"}
        widgets = {
            "username":forms.TextInput(attrs={"placeholder":"Enter valid username", "class":"form-control"}),
            "first_name":forms.TextInput(attrs={"placeholder":"Enter first name", "class":"form-control"}),
            "last_name":forms.TextInput(attrs={"placeholder":"Enter last name", "class":"form-control"}),
            "email":forms.EmailInput(attrs={"placeholder":"Enter Email ID", "class":"form-control"}),
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter valid username", "class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter valid password", "class":"form-control"}))
    class Meta:
        model = User


class ChangePassForm(PasswordChangeForm):
    old_password =forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={"placeholder":"Old password", "class":"form-control"}))
    new_password1 = forms.CharField(label="Set New Password", widget=forms.PasswordInput(attrs={"placeholder":"Set new password", "class":"form-control"}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={"placeholder":"Confirm new password", "class":"form-control"}))
    class Meta:
        model = User



class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }