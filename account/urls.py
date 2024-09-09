"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.authtoken import views
from .views import ListUserView, DetailUserView, UserRegistrationView, UserLoginView, Home


urlpatterns = [
    path('', ListUserView.as_view(), name='user-list'),
    # if custom user model is used then for user detail view, give name as model_name-detail
    path('<int:pk>/', DetailUserView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('success/', Home.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('api-token-auth/', views.obtain_auth_token, name='get-token'),
]
