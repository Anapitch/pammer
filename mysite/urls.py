from django.contrib import admin
from django.urls import path
from myapp import views as appview

urlpatterns = [
    path('admin/',admin.site.urls),
    path('insert',appview.insert),
    path('moon',appview.moon),
    path('google',appview.google),
    path('',appview.google),
    
]
