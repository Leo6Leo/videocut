from django.shortcuts import render
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
    urllib.request.urlretrieve(url_link, 'media/video.mp4')
    return HttpResponse("success")


def cut_video(request):
    os.chdir("C:\\pyproj\\uofthacks\\cut_core")
    os.system('ffmpeg -i video.mp4 -af silencedetect=noise=-30dB:d=0.2 -f null - 2> output.txt')
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

    main()

    return HttpResponse("cut_process")