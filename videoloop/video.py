from moviepy.editor import VideoFileClip


def clip_duration(file):
    clip = VideoFileClip(file)
    print(clip.duration)
