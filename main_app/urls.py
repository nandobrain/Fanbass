
from django.urls import path
from . import views


urlpatterns = [
   path('artist/', views.ArtistList.as_view(), name='artist_index'),
   path('artist/<int:pk>/', views.ArtistDetail.as_view, name='artist_detail'),
   path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
   path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
   path('artist/<int:pk>/delete/', views.ArtistDelete. as_view(), name='artist_delete'),
   path('artist/<int:artist_id>/add_photo/', views.add_photo, name='add_photo'),
   path('accounts/signup/', views.signup, name='signup'),
   path('', views.home, name='home'),
]
