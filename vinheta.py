from moviepy.editor import VideoFileClip, ColorClip, TextClip, CompositeVideoClip

#Função que retorna a velocidade e a posição da vinheta no vídeo
def pos(time):
    return (time*-350, 'bottom')
#Função que cria a vinheta e realiza a composição dela no video final
def cria_vinheta(arquivo):
    video = VideoFileClip(arquivo)
    duracao = video.duration
    video_vinheta = 'video_final_vinheta.mp4'
    #Abre o novo arquivo .csv apenas para leitura
    f = open('noticias-ifmt.csv', 'r')
    data = f.read().replace('\n', '')
    #Cria um clipe de texto
    text = TextClip(
        data, color = 'white',font = 'Arial', fontsize = 80
        ).set_duration(duracao)
    #Cria um clipe de cor
    color = ColorClip(
        text.size, color = (0, 128, 0), duration = duracao
    )
    #Concatena ambos os clipes e definem sua posição no vídeo
    cor_texto = CompositeVideoClip([color, text]).set_position(pos)
    compose = CompositeVideoClip([video, cor_texto])
    #Salva o resultado
    compose.write_videofile(video_vinheta)
