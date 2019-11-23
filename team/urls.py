from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'team'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.GameStatsView.as_view(), name='game-stats'),
    path('stats/', views.TeamStatsView.as_view(), name='stats'),
    path('games/', views.GamesView.as_view(), name='games'),
    path('players/', views.PlayersView.as_view(), name='players'),
    path('<slug:slug>/', views.PlayerDetailView.as_view(), name='detail'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

