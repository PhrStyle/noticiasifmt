from flask import Flask, render_template
import os
import json
import csv
import vlc

app = Flask(__name__)
app.debug = True

media_player = vlc.MediaListPlayer()
playlist_player = vlc.Instance()
media_list = playlist_player.media_list_new()
media = playlist_player.media_new('playlist.pls')
media_list.add_media(media)
media_player.set_media_list(media_list)

listagit = ""
listainsta = ""

@app.route("/")
def mainpage():
    listagit = sorted(os.listdir("noticiasifmt/static/github"))
    listainsta = sorted(os.listdir("noticiasifmt/static/ifmtcuiabaoficial"))
    itemgit = ""
    i = 0
    while itemgit == "":
        if ".jpeg" in listagit[i] or ".jpg" in listagit[i] or ".png" in listagit[i]:
            itemgit = '{"name":"' + listagit[i] + '", "tipo":"Imagem"}'
            itemgit = json.loads(itemgit)
        elif ".mp4" in listagit[i]:
            itemgit = '{"name":"' + listagit[i] + '", "tipo":"Video"}'
            itemgit = json.loads(itemgit)
        i = i + 1

    iteminsta = ""
    i = 0
    while iteminsta == "":
        if ".jpeg" in listainsta[i] or ".jpg" in listainsta[i] or ".png" in listainsta[i]:
            iteminsta = '{"name":"' + listainsta[i] + '", "tipo":"Imagem"}'
            iteminsta = json.loads(iteminsta)
        elif ".mp4" in listainsta[i]:
            iteminsta = '{"name":"' + listainsta[i] + '", "tipo":"Video"}'
            iteminsta = json.loads(iteminsta)
        i = i + 1

    arquivo = open('noticiasifmt/noticias-ifmt.csv')

    linhas = csv.reader(arquivo)

    noticias = []
    for linha in linhas:
        noticias.append(linha[0])

    media_player.play()
    return render_template(
        '/template.html',
	listagit=itemgit,
	listainsta=iteminsta,
        noticias=noticias,
    )

@app.route("/getlistagithub")
def listagit():
    listagit = sorted(os.listdir("noticiasifmt/static/github"))
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
    listainsta = os.listdir("noticiasifmt/static/ifmtcuiabaoficial")
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

@app.route("/pararradio")
def pararradio():
    media_player.pause()
    return ""

@app.route("/iniciarradio")
def iniciarradio():
    media_player.play()
    return ""

@app.route("/verificarlistas")
def verificarlistas():
    linsta = os.listdir("noticiasifmt/static/ifmtcuiabaoficial")
    lgit = sorted(os.listdir("noticiasifmt/static/github"))
    if linsta != listainsta or lgit != listagit:
        print("teste")
        return "teste"
    else:
        print("nao")
        return "nao"
    return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0')
