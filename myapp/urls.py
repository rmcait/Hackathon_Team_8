from django.contrib import admin
from django.urls import path, include
from .views import indexfunc, upload_image, process_image


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', indexfunc, name='index'),
    path("upload/", upload_image, name="upload_image"),
    path("process/", process_image, name="process_image"),
]
