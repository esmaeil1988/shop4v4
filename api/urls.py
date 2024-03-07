from django.urls import path
from.views import vproduct
from rest_framework.authtoken import views

urlpatterns = [
    path('product/',vproduct.as_view() ),
    path('login/', views.obtain_auth_token),
    
]
