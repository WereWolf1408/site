from django import forms


class AuthenticationForm(forms.Form):
     your_name = forms.CharField(label='Your name', max_length=50)
     your_name.widget = forms.TextInput(attrs={'class': 'auth_reg_input'})
     password = forms.CharField(label='Yor password', max_length=50)
     password.widget = forms.PasswordInput(attrs={'class': 'auth_reg_input', 'id': 'pass'})


class RegistrationForm(AuthenticationForm):
     confirm_pass = forms.CharField(max_length=50)
     confirm_pass.widget = forms.PasswordInput(attrs={'class': 'auth_reg_input', 'id': 'conf_pass'})
     emain = forms.EmailField(max_length=50)
     emain.widget = forms.TextInput(attrs={'class': 'auth_reg_input'})

