from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import urllib.request
import you_get

def index(request):
    return render(request,'index.html')


def download_video(request):
    url_link = request.POST["urlname"]
    urllib.request.urlretrieve(url_link, 'video_name.mp4')
    return HttpResponse("success")