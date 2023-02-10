from django.contrib import admin
from .models import Artist, Experience, Comment, Photo

# Register your models here.
admin.site.register(Artist)
admin.site.register(Experience)
admin.site.register(Comment)
admin.site.register(Photo)