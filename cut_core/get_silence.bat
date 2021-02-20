cd cut_core
ffmpeg -i video.mp4 -af silencedetect=noise=-30dB:d=0.2 -f null - 2> output.txt