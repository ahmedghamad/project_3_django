"""
URL configuration for book_finder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home_page.views import Recomended
from django.conf.urls.static import static
from home_page.views import home_view, Welcome_view

urlpatterns = [
    path('', Welcome_view, name='welcome'),
    path('home/', home_view, name='home'),
    path('', include('home_page.urls')),  # Include URLs from the home_page app
    path('accounts/', include('allauth.urls')),  # Include URLs for authentication
    path('recomended/', Recomended, name='recomended'),  # URL for recommended list
    path('admin/', admin.site.urls),  # Admin URL
    path('search/', home_view, name='search'),  # URL for search form handling
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)