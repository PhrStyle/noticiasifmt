from moviepy.editor import *
import os
#import vinheta

def concatenacao_final():
    fps = 30
    videos = []
    path = 'static/videos'
    video_final = 'video_final.mp4'
    clipes = []
    i = 0
    for video in os.listdir(path):
        videos.append((os.path.join(path, video)))
    tamanho = len(videos)
    for i in range(tamanho):
        clipes.append(VideoFileClip(videos[i]))
    final = concatenate_videoclips(clipes, method = 'compose')
    final.write_videofile(video_final, fps=fps)
    #Chama a função de criação da vinheta
    #vinheta.cria_vinheta(video_final)