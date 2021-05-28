"""task_app_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # to refer "urls.py" in api for task_app_api's "urls.py"
    path('api/', include('api.urls')),
    # To set a pass for return JWT TOKEN, also will implement page transition to JWT Authentication page.
    path('authen/', include('djoser.urls.jwt')),
]
# If when type media at the end of point as the path, it will refer content of media folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
