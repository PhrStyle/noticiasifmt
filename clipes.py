from os import walk
from moviepy.editor import *
import os
#import concatenacao_video_final

#Função responsável por criar os clipes de vídeo das imagens da pasta do Instagram e da pasta do GitHub
def cria_clipes():
    files_insta = []
    files_git = []
    images_list_insta = []
    images_list_git = []
    path_pasta_instagram = 'static/ifmtcuiabaoficial'
    path_pasta_git = 'github'
    path_videos = 'static/videos'
    qtd_imagens_insta = 0
    qtd_imagens_git = 0
    tempo_base = 6
    fps = 30
    for (dirpath, dirnames, filenames_insta) in walk(path_pasta_instagram):
        files_insta.extend(filenames_insta)
        break
    tamanho_files_insta = len(files_insta)
    #Cria uma lista com as imagens da pasta do Instagram
    for i in range(tamanho_files_insta):
        if files_insta[i].endswith('.jpg') or files_insta[i].endswith('.png'):
            qtd_imagens_insta+=1
            images_list_insta.append(os.path.join(path_pasta_instagram, files_insta[i]))
        #Os videos são salvos em outro diretório
        elif files_insta[i].endswith('.mp4'):
            if os.path.exists(path_videos):
                video = VideoFileClip(os.path.join(path_pasta_instagram, files_insta[i]))
                new = video.without_audio()
                new.write_videofile(os.path.join(path_videos, files_insta[i]))
    for (dirpath, dirnames, filenames_git) in walk(path_pasta_git):
        files_git.extend(filenames_git)
        break
    tamanho_files_git = len(files_git)
    #Cria uma lista com as imagens da pasta do GitHub
    for i in range(tamanho_files_git):
        if files_git[i].endswith('.jpg') or files_git[i].endswith('.png'):
            qtd_imagens_git+=1
            images_list_git.append(os.path.join(path_pasta_git, files_git[i]))
        #Os videos são salvos em outro diretório
        elif files_git[i].endswith('.mp4'):
            if os.path.exists(path_videos):
                video = VideoFileClip(os.path.join(path_pasta_git, files_git[i]))
                new = video.without_audio()
                new.write_videofile(os.path.join(path_videos, files_git[i]))
    '''
    #Se a quantidade de imagens do Instagram for maior, elas que irão definir o tempo de duração do vídeo (tempo_base*qtd_imagens_insta)
    #E cada imagem do GitHub terá uma duração definida pelo produto entre a quantidade de vezes que é menor e o tempo base (6 segundos)
    if qtd_imagens_insta > qtd_imagens_git and qtd_imagens_git > 0:
        div = (qtd_imagens_insta)/(qtd_imagens_git)
        tempo_insta = tempo_base
        tempo_git = tempo_base*div
    else:
        tempo_insta = tempo_base
        if qtd_imagens_git > qtd_imagens_insta and qtd_imagens_insta > 0:
    #Se a quantidade de imagens do GitHub for maior, elas que irão definir o tempo de duração do vídeo (tempo_base*qtd_imagens_dep)
    #E cada imagem do Instagram terá uma duração definida pelo produto entre a quantidade de vezes que é menor e o tempo base (6 segundos)
            div = (qtd_imagens_git)/(qtd_imagens_insta)
            tempo_git = tempo_base
            tempo_insta = tempo_base*div
        else:
            tempo_git = tempo_base
    '''
    #Se houver imagens de ambos os diretórios      
    if qtd_imagens_git > 0 and qtd_imagens_insta > 0:
        #Cria um clipe com as imagens do Instagram, definindo seu tempo de tela
        #clipe_imagens_insta = [ImageClip(m).set_duration(tempo_insta) for m in images_list_insta]
        clipe_imagens_insta = [ImageClip(m).set_duration(tempo_base) for m in images_list_insta]
        concat_clipe_imagens_insta = concatenate_videoclips(clipe_imagens_insta, method = 'compose')
        #Salva o clipe
        concat_clipe_imagens_insta.write_videofile('clipe_imagens_insta.mp4', fps=fps)
        #Cria um clipe com as imagens do GitHub, definindo seu tempo de tela
        #clipe_imagens_git = [ImageClip(n).set_duration(tempo_git) for n in images_list_git]
        clipe_imagens_git = [ImageClip(n).set_duration(tempo_base) for n in images_list_git]
        concat_clipe_imagens_git = concatenate_videoclips(clipe_imagens_git, method = 'compose')
        #Salva o clipe
        concat_clipe_imagens_git.write_videofile('clipe_imagens_git.mp4', fps=fps)
        
        #clipe_git = VideoFileClip('clipe_imagens_git.mp4').margin(10)
        #clipe_insta = VideoFileClip('clipe_imagens_insta.mp4').margin(10)
        clipe_git = VideoFileClip('clipe_imagens_git.mp4').resize((1200,800))
        clipe_insta = VideoFileClip('clipe_imagens_insta.mp4').resize((1200,800))
        #clipes = clips_array([[clipe_git,clipe_insta]])
        clipes = concatenate_videoclips([clipe_git, clipe_insta], method = 'compose')
        clipes.write_videofile(os.path.join(path_videos, 'clipes_concatenados.mp4'), fps=fps)
        #Chama a função responsável por concatenar os clipes criados
        #concatenacao_video_final.concatenacao_final()

    #Se houver apenas imagens do GitHub
    elif qtd_imagens_git > 0 and qtd_imagens_insta == 0:
        #Cria um clipe com as imagens do GitHub, definindo seu tempo de tela
        clipe_imagens_git = [ImageClip(n).set_duration(tempo_base) for n in images_list_git] 
        concat_clipe_imagens_git = concatenate_videoclips(clipe_imagens_git, method = 'compose')     
        clipe_git = concat_clipe_imagens_git.resize((1200,800))
        clipe_git.write_videofile(os.path.join(path_videos, 'clipes_concatenados.mp4'), fps=fps)
        #Chama a função responsável por concatenar o clipe criado
        #concatenacao_video_final.concatenacao_final()

    #Se houver apenas imagens do Instagram
    elif qtd_imagens_insta > 0 and qtd_imagens_git == 0:
        #Cria um clipe com as imagens do Instagram, definindo seu tempo de tela
        clipe_imagens_insta = [ImageClip(m).set_duration(tempo_base) for m in images_list_insta]  
        concat_clipe_imagens_insta = concatenate_videoclips(clipe_imagens_insta, method = 'compose')
        clipe_insta = concat_clipe_imagens_insta.resize((1200,800))
        clipe_insta.write_videofile(os.path.join(path_videos, 'clipes_concatenados.mp4'), fps=fps)
        #Chama a função resposável por concatenar o clipe criado
        #concatenacao_video_final.concatenacao_final()
