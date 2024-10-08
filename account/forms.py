from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
