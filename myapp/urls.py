from django.contrib import admin
from django.urls import path, include
from .views import indexfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', indexfunc, name='index'),
]