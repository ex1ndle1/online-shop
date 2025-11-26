from django import forms
from .models import User



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,  label='enter password')
    password_confirm = forms.CharField(widget=forms.PasswordInput,  label='confirm your password')


    class Meta:
        model = User
        exclude = ()

    def clean(self):  #added clean method for comparing two passwords 
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('passwords are diffrent')
        
        return cleaned_data