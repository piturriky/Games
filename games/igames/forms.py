from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Game,Platform,Company
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
	user.first_name = self.cleaned_data["first_name"]
	user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class GameForm(forms.ModelForm):
	release_date = forms.DateField(widget=SelectDateWidget(years=range(date.today().year,1980,-1)))
	class Meta:
		model = Game

class CompanyForm(forms.ModelForm):
	fundation_date = forms.DateField(widget=SelectDateWidget(years=range(date.today().year,1900,-1)))
	class Meta:
		model = Company

class PlatformForm(forms.ModelForm):
	class Meta:
		model = Platform

