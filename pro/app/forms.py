from django import forms
from .models import TODO, CustomUser
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'image', 'birthday']

        


class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'memo', 'important']
        
class TODOFormCaptcha(forms.ModelForm):
    captcha = CaptchaField(generator='captcha.helpers.math_challenge')
    class Meta:
        model = TODO
        fields = ['title', 'memo', 'important', 'captcha']

