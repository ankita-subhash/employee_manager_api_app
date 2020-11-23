from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from staff.models import ManagerInfo, EmpInfo



class ManagerForm(ModelForm):
    class Meta:
        model = ManagerInfo
        exclude = ('payment_status', 'user', 'email')

class EmpForm(ModelForm):
	class Meta:
		model = EmpInfo
		exclude = ( 'emp_pwd', 'manager_user')
		

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = [ 'username', 'password1', 'password2', 'email']
		widgets = {
                'username': forms.TextInput(attrs={'class': 'form-group', }),
				'email': forms.TextInput(attrs={'class': 'form-group', }),
				'password1': forms.TextInput(attrs={'class': 'form-group', }),
				'password2': forms.TextInput(attrs={'class': 'form-group', }),
			}

