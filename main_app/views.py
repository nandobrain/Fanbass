
import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Artist, Experience, User, Photo
from .forms import CommentForm


# Create your views here.



class ArtistDetail(DetailView):
   model = Artist
   template_name = 'artists/artist_details.html'
 
class ArtistList(ListView):
   model = Artist  
   template_name = 'artists/artist_list.html'

class ArtistCreate(CreateView):
   model = Artist
   fields = ['name']
   success_url = '/artists'

   def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)


class ArtistUpdate(UpdateView):
   model = Artist
   fields =  ['members', 'description']


class ArtistDelete(DeleteView):
   model = Artist
   success_url = '/artists'



class ExperienceList(ListView):
   model = Experience


class ExperinceDetail(DetailView):
   model = Experience
   
class ExperienceCreate(CreateView):
   model = Experience
   fields = ['Music', 'Video', 'Show', 'Merchandise', 'Social Media', 'News']

class ExperienceUpdate(UpdateView):
   model = Experience
   fields = '__all__'

class ExperienceDelete(DeleteView):
   model = Experience
   success_url = '/experience'



def add_comment(request, experience_id):
   form = CommentForm(request.POST)
   if form.is_vali():
      new_comment = form.save(commit=False)
      new_comment.experience_id = experience_id
      new_comment.save()
   return redirect('experince_detail', experience_id=experience_id)




def add_photo(request, artist_id):
   photo_file = request.FILES.get('photo-file', None)
   if photo_file:
       s3 = boto3.client('s3')
       key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
       try:
           bucket = os.environ['S3_BUCKET']
           s3.upload_fileobj(photo_file, bucket, key)
           url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
           Photo.objects.create(url=url, artist_id=artist_id)
       except Exception as e:
           print('An error occurred uploading file to S3')
           print(e)
   return redirect('detail', artist_id=artist_id)




def signup(request):
 error_message = ''
 if request.method == 'POST':
   form = UserCreationForm(request.POST)
   if form.is_valid():
     user = form.save()
     login(request, user)
     return redirect('index')
   else:
     error_message = 'Invalid sign up - try again'
 form = UserCreationForm()
 context = {'form': form, 'error_message': error_message}
 return render(request, 'registration/signup.html', context)


def home(request):
   return render(request, 'home.html')

