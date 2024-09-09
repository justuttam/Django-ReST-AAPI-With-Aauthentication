from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .forms import RegisterForm
from .models import User
from .serializers import UserSerializer, CreateUserSerializer


class Home(TemplateView):
    template_name = 'account/home.html'


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserRegistrationView(generics.CreateAPIView):
#     serializer_class = CreateUserSerializer
#
#     permission_classes = [permissions.AllowAny]
class UserRegistrationView(CreateView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.request.session['username'] = form.cleaned_data.get('username')
        self.request.session['token'] = "abc"
        return super().form_valid(form)


class UserLoginView(views.APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
