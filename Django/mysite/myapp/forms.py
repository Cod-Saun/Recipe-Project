from django import forms

class PlaylistForm(forms.Form):
    Song_Name = forms.CharField(label='Song Name', max_length=40)
    Artist_Name = forms.CharField(label='Artist Name', max_length=30)
    Album_Name = forms.CharField(label='Album Name', max_length=30)
    Song_Duration = forms.CharField(label='Song Duration', max_length=5)
