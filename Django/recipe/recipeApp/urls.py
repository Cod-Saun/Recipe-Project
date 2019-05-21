from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.Homepage),
        path('gallery', views.Gallery),
        path('galleryitems', views.Gallery_Json),
        path('login/', auth_views.LoginView.as_view()),
        path('logout', views.Logout),
        path('register', views.Register),
        path('recommendation', views.Recommendation),
        path('search/', views.Search),
        path('submit/', views.Submit),
        path('chat/', views.Chat),
        path('chat/<slug:room_name>/', views.ChatRoom),
        #url(r'^(?P<room_name>[^/]+)/$', views.ChatRoom, name='room'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
