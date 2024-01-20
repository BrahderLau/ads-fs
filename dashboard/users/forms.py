from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
 
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]