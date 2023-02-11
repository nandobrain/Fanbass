
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


# Create your views here.



class ArtistDetail(DetailView):
   model = Artist
 
class ArtistList(ListView):
   model = Artist  
  


class ArtistCreate(CreateView):
   model = Artist
   fields = ['name', 'members', 'description']


   # def from_valid(self, form):
   #     form.instance.user = self.request.user
   #     return super().form_valid(form)


class ArtistUpdate(UpdateView):
   model = Artist
   fields =  ['members', 'description']


class ArtistDelete(DeleteView):
   model = Artist
   success_url = '/artist'










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

