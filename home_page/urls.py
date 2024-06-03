from django.urls import path
from .views import home_view, Recomended, Welcome_view


urlpatterns = [
    path('search/', home_view, name='search'),
    path('recomended/', Recomended, name='recomended'),
    path('welcome/', Welcome_view, name='welcome'),
    
    # Other URLs...
]