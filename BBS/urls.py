from django.urls import include, path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('accounts/', include('allauth.urls')),
]
