
from django.urls import path
from . import views

urlpatterns = [
   path('artists/', views.ArtistList.as_view(), name='artist_index'),
   path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist_details'),
   path('artists/create/', views.ArtistCreate.as_view(), name='artist_create'),
   path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
   path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
   path('artists/<int:pk>/', views.ExperienceList.as_view(), name='experience_details'),
   path('artists/<int:pk>/experiences/create/', views.ExperienceCreate.as_view(), name='experience_create'),
   path('artists/<int:pk>/experiences/<int:experience_id>/update/', views.ExperienceUpdate.as_view(), name='experience_update'),
   path('experiences/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='experience_delete'),
   path('artists/<int:pk>/comments/create/', views.CommentCreate.as_view(), name='comment_create'),
   path('accounts/signup/', views.signup, name='signup'),
   path('', views.home, name='home'),
]

