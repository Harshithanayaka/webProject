from offers.models import plans
from offers.models import postpaid
from offers.models import dongle
from offers.models import userdetails
from offers.models import invoice
from django import forms
from offers.models import newconnection
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class PlanForm(forms.ModelForm):
    class Meta:
        model = plans
        fields = "__all__"

class PostpaidForm(forms.ModelForm):
    class Meta:
        model=postpaid
        fields="__all__"

class DongleForm(forms.ModelForm):
    class Meta:
        model=dongle
        fields="__all__"

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = userdetails
        fields = "__all__"
class NewConnectionForm(forms.ModelForm):
    class Meta:
        model = newconnection
        fields = "__all__"
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = invoice
        fields = "__all__"