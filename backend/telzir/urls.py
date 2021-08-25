"""telzir URL Configuration

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
from django.urls import include, path
from rest_framework import routers

from calls.api import view as callsviewsets
from users.api import view

route = routers.DefaultRouter()

route.register(r"calls", callsviewsets.CallsViewSet, basename="calls")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", view.CreateUserView.as_view(), name="create"),
    path("token/", view.CreateTokenView.as_view(), name="token"),
    path("me/", view.ManageUserView.as_view(), name="me"),
    path("", include(route.urls)),
]
