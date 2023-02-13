
from django.urls import path
from . import views



urlpatterns = [
   path('artists/', views.ArtistList.as_view(), name='artist_index'),
   path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist_details'),
   path('artists/create/', views.ArtistCreate.as_view(), name='artist_create'),
   path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
   path('artists/<int:pk>/delete/', views.ArtistDelete. as_view(), name='artist_delete'),
   path('artists/<int:artist_id>/add_photo/', views.add_photo, name='add_photo'),
   path('accounts/signup/', views.signup, name='signup'),
   path('', views.home, name='home'),
]