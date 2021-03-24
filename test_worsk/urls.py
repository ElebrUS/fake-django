"""test_worsk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from users.views import signup, home
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as a_vs
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
    url(r'^logout/$', LogoutView.as_view(next_page='login'), name='logout'),
    url(r'^signup/$', signup, name='signup'),
    path('csv/', include('schemas.urls'), name='csv_index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
