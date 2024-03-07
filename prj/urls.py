from django.contrib import admin
from django.urls import path,include
from app1.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('login/',login),
    path('logout/',lout),
    path('error/',error),
    path('register/',reg),
    path('success/',sc),
    path('showproduct/<adad>',showprod),
    path('allprod/',allprod),
    path('showcategory/<adad>',showcategory),
    path('contact/',contactus),
    path('addtocart/<adad>',addtocart),
    path('delcart/<adad>',delcart),
    path('cart/',showcart),
    path('editqnt/<adad>',editqnt),
    path('api/',include("api.urls")),
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
