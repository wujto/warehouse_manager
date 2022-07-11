from warehouse_manager_base.models import CustomUserModel
from django import forms

class UserUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, max_length=25, required= False)
    new_password = forms.CharField(widget=forms.PasswordInput, max_length=25,required = False)
    new_password2 = forms.CharField(widget=forms.PasswordInput, max_length=25,required = False)
    phone_number = forms.CharField(max_length=9, min_length=9, required=False)

