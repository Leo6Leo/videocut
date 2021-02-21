from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
import urllib.request
import os
from cut_core.cut import main


import shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips


def index(request):
    return render(request,'home.html')


def download_video(request):
    url_link = request.POST["urlname"]
    urllib.request.urlretrieve(url_link, './static/video.mp4')
    return render(request,"success.html")


def cut_video(request):
    os.chdir("C:\\pyproj\\uofthacks\\static")
    os.system('ffmpeg -i video.mp4 -af silencedetect=noise=-20dB:d=0.2 -f null - 2> output.txt')
    # read txt method one
    f = open("./output.txt")
    f_out = open('./out.txt', 'w')
    line = f.readline()
    while line:
        if "silence_end" in line:
            haha = line.split("silence_end:")[1]
            haha3 = haha.split(" |")[0]
            haha2 = haha.split("silence_duration: ")[1]
            haha4 = haha2.split("\n")[0]

            print(haha3 + " " + haha4)
            f_out.write(haha3 + " " + haha4)
            f_out.write("\n")
        line = f.readline()
    f.close()
    f_out.close()

    main()

    return redirect("main:result")

def result(request):
    return render(request,"result.html")

def about(request):
    return render(request,"about.html")