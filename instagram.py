from instaloader import Instaloader, Profile
from datetime import datetime, timedelta
import correcao_pasta_instagram
import os
import pathlib

#Função responsável por executar o download das publicações do Instagram Oficial do IFMT
def download_instagram():
    #Realiza o download das publicações dos últimos 5 dias
    data_inicio = datetime.today() - timedelta(days=5)
    L=Instaloader()
    PROFILE = 'ifmtcuiabaoficial'
    profile = Profile.from_username(L.context, PROFILE)
    post_sorted = sorted(profile.get_posts(),key=lambda post: post.likes, reverse=True)
    for post in post_sorted:
        #Faz o download das publicações que estão dentro do prazo estabelecido e as que estão fixadas
        if post.date >= data_inicio or post.is_pinned:
            L.download_post(post, pathlib.Path('static/ifmtcuiabaoficial'))
    #Chama a função de correção da pasta com os arquivos do Instagram
    correcao_pasta_instagram.correcao_pasta()
