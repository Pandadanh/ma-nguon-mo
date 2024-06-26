from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'image', 'audio_file', 'audio_link', 'lyrics', 'duration']
