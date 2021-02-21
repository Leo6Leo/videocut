import sys
import subprocess
import os
import shutil
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Input path
input_file = "../static/video.mp4"
# Output path
output_file = "../static/edited.mp4"
# Silence timestamps file
silence_file = "out.txt"

# Ease in duration between cuts
try:
    ease = float(sys.argv[4])
except IndexError:
    ease = 0.0

minimum_duration = 1.0

def main():
    count = 0
    last = 0
    opened_file = open(silence_file, "r", errors='replace')
    video = VideoFileClip(input_file)
    whole_duration = video.duration
    clips = []
    while True:
        line = opened_file.readline()

        if not line:
            break

        end,duration = line.strip().split()

        to = float(end) - float(duration)

        start = float(last)
        clip_duration = float(to) - start

        print("Video length: {} seconds".format(clip_duration))

        if clip_duration < minimum_duration:
            continue

        if whole_duration - to < minimum_duration:
            continue

        if start > ease:
            start -= ease

        print("Silence {} (Start: {}, End: {})".format(count, start, to))
        clip = video.subclip(start, to)
        clips.append(clip)
        last = end
        count += 1

    if whole_duration - float(last) > minimum_duration:
        print("Silence {} (Start: {}, End: {})".format(count, last, 'EOF'))
        clips.append(video.subclip(float(last)-ease))

    processed_video = concatenate_videoclips(clips)
    processed_video.write_videofile(
        output_file,
        fps=60,
        preset='ultrafast',
        codec='libx264'
    )

    opened_file.close()
    video.close()

