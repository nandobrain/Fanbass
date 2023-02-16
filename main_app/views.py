
import uuid
import boto3
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Artist, Experience, User, Comment
from .forms import CommentForm, ExperienceForm
from django.urls import reverse

# Create your views here.

class ArtistDetail(DetailView):
   model = Artist
   template_name = 'artists/artist_details.html'
   def get_context_data(self, **kwargs):
      context = super(ArtistDetail, self).get_context_data(**kwargs)
      context['experience_form'] = ExperienceForm()
      context['comment_form'] = CommentForm()
      return context

class ArtistList(ListView):
   model = Artist  
   template_name = 'artists/artist_list.html'

   def get_queryset(self):
        queryset = super(ArtistList, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

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


class ExperienceDetail(DetailView):
   model = Experience


class ExperienceCreate(CreateView):
   model = Experience
   fields = ['experience_type','user_review', 'date_time', 'link', 'music_type', 'show_venue_name']

   def get_success_url(self):
      pk = self.kwargs['pk']
      return reverse('artist_details', kwargs={'pk': pk})

   def form_valid(self, form):
      form.instance.user = self.request.user
      pk = self.kwargs['pk']
      artist = Artist.objects.get(id=pk)
      form.instance.artist = artist

      self.object = form.save()
      photo_file = form.files.get('photo-file', None)
      if photo_file:
         s3 = boto3.client('s3')
         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
         try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, experience_id=self.object.id)
         except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
      return HttpResponseRedirect(self.get_success_url()) 
   

class ExperienceUpdate(UpdateView):
   model = Experience
   fields = '__all__'

   def get_context_data(self, **kwargs):
      context = super(ExperienceUpdate, self).get_context_data(**kwargs)
      context['experience_form'] = ExperienceForm()
      return context

   def get_success_url(self):
    artist = self.object.artist 
    return reverse( 'artist_details', kwargs={'pk': artist.pk})

class ExperienceDelete(DeleteView):
   model = Experience
   
   def get_success_url(self):
      artist = self.object.artist 
      return reverse('artist_details', kwargs={'pk' : artist.id})


class CommentCreate(CreateView):
   model = Comment
   fields = ['comment']

   def form_valid(self, form):
      form.instance.user = self.request.user
      pk = self.kwargs['pk']
      artist = Artist.objects.get(id=pk)
      form.instance.artist = artist
      form.instance.user = self.request.user
      return super().form_valid(form)

   def get_success_url(self):
      pk = self.kwargs['pk']
      return reverse('artist_details', kwargs={'pk': pk})


class CommentUpdate(UpdateView):
   model = Comment
   fields = ['comment']
   
   def get_success_url(self):
      artist = self.object.artist 
      return reverse('artist_details', kwargs={'pk' : artist.id})

class CommentDelete(DeleteView):
   model = Comment

   def get_success_url(self):
      artist = self.object.artist 
      return reverse('artist_details', kwargs={'pk' : artist.id})

def signup(request):
 error_message = ''
 if request.method == 'POST':
   form = UserCreationForm(request.POST)
   if form.is_valid():
     user = form.save()
     login(request, user)
     return redirect('artist_index')
   else:
     error_message = 'Invalid sign up - try again'
 form = UserCreationForm()
 context = {'form': form, 'error_message': error_message}
 return render(request, 'registration/signup.html', context)

def home(request):
   return render(request, 'home.html')