from django import forms
from .models import User



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,  label='enter password')
    password_confirm = forms.CharField(widget=forms.PasswordInput,  label='confirm your password')


    class Meta:
        model = User
        fields = ("username", "email", "phone")

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get("password") != cleaned_data.get("password_confirm"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

        
        
    def save(self, commit=True):
       user = super().save(commit=False)
       user.set_password(self.cleaned_data["password"])  # hash password

       if commit:
        user.save()
       return user
    

class LoginForm(forms.Form):
     username = forms.CharField(label="enter username")
     password = forms.CharField(widget=forms.PasswordInput)