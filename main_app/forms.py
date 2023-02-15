from django.forms import ModelForm
from . models import Comment, Experience

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ExperienceForm(ModelForm):
  class Meta:
    model = Experience
    fields = ['experience_type', 'user_review', 'date_time', 'link', 'music_type', 'show_venue_name']