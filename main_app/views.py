from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login

from .models import Experience

# Create your views here.

class AristCreate(CreateView):
    model = Experience
    field = '__all__'

class ArtistDetail(DetailView):
    model = Experience

class ArtistUpdate(UpdateView):
    model = Experience
    field = '__all__'

class AristDelete(DeleteView):
    model = Experience
    field= '/artist'






