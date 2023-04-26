import wget
import os

#Função responsável pelo download da playlist da rádio
def download_playlist():
    playlist = 'playlist.pls'
    #Exclui a playlist anterior, se existir
    if(os.path.exists(playlist)):
        os.remove(playlist)
    #URL da playlist Web Rádio do IFMT
    playlist_url = 'https://player.hdradios.net/player/6990'
    wget.download(playlist_url , playlist)