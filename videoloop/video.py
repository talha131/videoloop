from moviepy.editor import VideoFileClip, CompositeVideoClip, transfx


def clip_duration(file):
    clip = VideoFileClip(file)
    return clip.duration


def concat_video(file, count, td):
    d = clip_duration(file)
    video = CompositeVideoClip([VideoFileClip(file).set_start(
        (d * i) - (td * i)).fx(transfx.crossfadein, td * (0 if i == 0 else 1)) for i in range(0, count)])
    video.write_videofile("27B-concat-3600.mp4")
