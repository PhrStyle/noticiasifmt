from instaloader import Instaloader, Profile
from datetime import datetime, timedelta
import os
from os import walk
import pathlib

#Função responsável por executar o download das publicações do Instagram Oficial do IFMT
def download_instagram():
    #Realiza o download das publicações dos últimos 5 dias
    data_inicio = datetime.today() - timedelta(days=6)
    L=Instaloader()
    PROFILE = 'ifmtcuiabaoficial'
    profile = Profile.from_username(L.context, PROFILE)
    post_sorted = sorted(profile.get_posts(),key=lambda post: post.likes, reverse=True)
    for post in post_sorted:
        #Faz o download das publicações que estão dentro do prazo estabelecido e as que estão fixadas
        if post.date >= data_inicio or post.is_pinned:
            L.download_post(post, pathlib.Path('static/ifmtcuiabaoficial'))
    #Chama a função de correção da pasta com os arquivos do Instagram
    correcao_pasta()

def correcao_pasta():
    files = []
    path = 'static/ifmtcuiabaoficial'
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        break
    tamanho = len(files)
    for i in range(tamanho):
        #Se existir um arquivo .mp4, ele busca o arquivo .jpg com o mesmo nome
        if files[i].endswith('.mp4'):
            aux1 = os.path.splitext(files[i])[0]
            for j in range(tamanho):
                if files[j].endswith('.jpg'):
                    aux2 = os.path.splitext(files[j])[0]
                    #Se existir um arquivo .jpg (frame inicial do .mp4), ele é excluído
                    if aux2 == aux1:
                        lix = os.path.join(path, files[j])
                        if os.path.isfile(files[j]) == False:
                            os.remove(lix)
    #Busca todos os arquivos da pasta ifmtcuiabaoficial
    listainsta = os.listdir("static/ifmtcuiabaoficial")
    for l in listainsta:
        #remove todos os arquivos que nao sao videos/imagens
        if ".mp4" not in l and ".jpg" not in l and ".jpeg" not in l and ".png" not in l:
            os.remove("static/ifmtcuiabaoficial/" + l)
