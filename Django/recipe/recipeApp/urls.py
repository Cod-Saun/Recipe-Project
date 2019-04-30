from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.Homepage),
        path('recipes', views.Recipes),
        path('login', auth_views.LoginView.as_view()),
        path('logout', views.Logout),
        path('register', views.Register),
        path('recommendation', views.Recommendation),
        ]
