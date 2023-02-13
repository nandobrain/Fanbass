
from django.urls import path
from . import views


urlpatterns = [
   path('artist/', views.ArtistList.as_view(), name='artist_index'),
   path('artist/<int:pk>/', views.ArtistDetail.as_view(), name='artist_detail'),
   path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
   path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
   path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
   path('artist/<int:artist_id>/', views.ExperienceList.as_view(), name='experience_detail'),
   path('artist/<int:artist_id>/experience/<int:experience_id>/create/', views.ExperienceCreate.as_view(), name='experience_create'),
   path('artist/<int:artist_id/experience/<int:experience_id>/update/', views.ExperienceUpdate.as_view(), name='experience_update'),
   path('artist/<int:artist_id>/experience/<int:experience_id>/delete/', views.ExperienceDelete.as_view(), name='experience_delete'),
   path('artist/<int:artist_id>/add_photo/', views.add_photo, name='add_photo'),
   path('artist/<int:artist_id>/experience/<int:experience_id>/add_comment/', views.add_comment, name='add_comment'),
   path('accounts/signup/', views.signup, name='signup'),
   path('', views.home, name='home'),
]
