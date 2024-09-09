"""
URL configuration for Item app.

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
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('items/', views.ListItemView.as_view(), name='item-list'),
    path('items/<slug:item_slug>/', views.DetailItemView.as_view(), name='item-detail'),


    # path('cafes/search/<str:name>/', views.search_cafe, name='search-cafe'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
