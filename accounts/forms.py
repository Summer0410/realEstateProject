from django import forms

class registerForm(forms.Form):
    first_name = forms.CharField(label = "First name", max_length = 20)
    last_name = forms.CharField(label = "Last name", max_length = 20)
    email_address = forms.CharField(label = "Email address", max_length = 50)
    password = forms.CharField(label = "Password", max_length = 50)
    confirm_password = forms.CharField(label = "Confirm password", max_length = 20)

class LoginForm(forms.Form):
    email_address = forms.CharField(label = "Email address", max_length = 50)
    password = forms.CharField(label = "Password", max_length = 50)
    


    

