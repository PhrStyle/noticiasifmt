import os
from os import walk
#import clipes

#Função responsável por corrigir a falha de download dos arquivos .mp4
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
    listainsta = os.listdir("./static/ifmtcuiabaoficial")
    for l in listainsta:
        #remove todos os arquivos que nao sao videos/imagens
        if ".mp4" not in l and ".jpg" not in l and ".jpeg" not in l and ".png" not in l:
            os.remove("static/ifmtcuiabaoficial/" + l)
