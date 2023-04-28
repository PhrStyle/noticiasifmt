from flask import Flask, render_template
import os
import json
import csv
import vlc

app = Flask(__name__)
app.debug = True
@app.route("/")

def mainpage():
    listagit = sorted(os.listdir("./static/github"))
    listainsta = os.listdir("./static/ifmtcuiabaoficial")
    itemgit = ""
    i = 0
    while itemgit == "":
        i = i + 1
        if ".jpeg" in listagit[i] or ".jpg" in listagit[i] or ".png" in listagit[i]:
            itemgit = '{"name":"' + listagit[i] + '", "tipo":"Imagem"}'
            itemgit = json.loads(itemgit)
        else:
            itemgit = '{"name":"' + listagit[i] + '", "tipo":"Video"}'
            itemgit = json.loads(itemgit)

    iteminsta = ""
    i = 0
    while iteminsta == "":
        i = i + 1
        if ".jpeg" in listainsta[i] or ".jpg" in listainsta[i] or ".png" in listainsta[i]:
            iteminsta = '{"name":"' + listainsta[i] + '", "tipo":"Imagem"}'
            iteminsta = json.loads(iteminsta)
        elif ".mp4" in listainsta[i]:
            iteminsta = '{"name":"' + listainsta[i] + '", "tipo":"Video"}'
            iteminsta = json.loads(iteminsta)

    arquivo = open('noticias-ifmt.csv')

    linhas = csv.reader(arquivo)

    noticias = []
    for linha in linhas:
        noticias.append(linha[0])

    media_player = vlc.MediaListPlayer()
    playlist_player = vlc.Instance()
    media_list = playlist_player.media_list_new()
    media = playlist_player.media_new('playlist.pls')
    media_list.add_media(media) 
    media_player.set_media_list(media_list)
    media_player.play()
    return render_template(
        '/template.html',
	listagit=itemgit,
	listainsta=iteminsta,
        noticias=noticias,
    )

@app.route("/getlistagithub")
def listagit():
    listagit = sorted(os.listdir("./static/github"))
    lgit = []
    for l in listagit:
        if ".jpeg" in l or ".jpg" in l or ".png" in l:
            itemgit = '{"name":"' + l + '", "tipo":"Imagem"}'
        else:
            itemgit = '{"name":"' + l + '", "tipo":"Video"}'
        itemgit = json.loads(itemgit)
        if ".git" not in l:
            lgit.append(itemgit)
    lista = {"imgvid": lgit}
    return json.dumps(lista)

@app.route("/getlistainstagram")
def listainsta():
    listainsta = os.listdir("./static/ifmtcuiabaoficial")
    linsta = []
    for l in listainsta:
        if ".jpeg" in l or ".jpg" in l or ".png" in l:
            iteminsta = '{"name":"' + l + '", "tipo":"Imagem"}'
        elif ".mp4" in l:
            iteminsta = '{"name":"' + l + '", "tipo":"Video"}'
        if ".jpeg" in l or ".jpg" in l or ".png" in l or ".mp4" in l:
            iteminsta = json.loads(iteminsta)
            linsta.append(iteminsta)
    lista = {"imgvid": linsta}
    return json.dumps(lista)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
