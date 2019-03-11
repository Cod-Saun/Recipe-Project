from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import models
from . import forms

# Create your views here.

def index(request):
    i_list=models.Playlist.objects.all()
    i_form = forms.PlaylistForm()

    if request.method == "POST":
        i_form = forms.PlaylistForm(request.POST)
        if i_form.is_valid():
            new_playlist = models.Playlist()
            new_playlist.Song_Name = i_form.cleaned_data["Song_Name"]
            new_playlist.Artist_Name = i_form.cleaned_data["Artist_Name"]
            new_playlist.Album_Name = i_form.cleaned_data["Album_Name"]
            new_playlist.Song_Duration = i_form.cleaned_data["Song_Duration"]
            new_playlist.save()
            i_form = forms.PlaylistForm()
    else:
        i_form = forms.PlaylistForm()

    context = {
        "body":"Add Songs to the list to create a Playlist. Javascript will automatically update the playlist if something is added.",
        "item_list":i_list,
        "form":i_form
    }
    return render(request,"index.html", context=context)

def  playlist_json(request):
    i_list=models.Playlist.objects.all()
    response_list = {}
    response_list["Playlist"]=[]
    for item in i_list:
        response_list["Playlist"]+=[{"Song_Name":item.Song_Name}]
    return JsonResponse(response_list)
