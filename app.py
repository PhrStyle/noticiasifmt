from flask import Flask, render_template
import os
import json

app = Flask(__name__)
app.debug = True
@app.route("/")

def mainpage():
    listagit = os.listdir("./static/github")
    listainsta = os.listdir("./static/ifmtcuiabaoficial")
    if ".jpeg" in listagit[0] or ".jpg" in listagit[0] or ".png" in listagit[0]:
        itemgit = '{"name":"' + listagit[0] + '", "tipo":"Imagem"}'
    else:
        itemgit = '{"name":"' + listagit[0] + '", "tipo":"Video"}'
    itemgit = json.loads(itemgit)

    if ".jpeg" in listainsta[0] or ".jpg" in listainsta[0] or ".png" in listainsta[0]:
        iteminsta = '{"name":"' + listainsta[0] + '", "tipo":"Imagem"}'
    else:
        iteminsta = '{"name":"' + listainsta[0] + '", "tipo":"Video"}'
    iteminsta = json.loads(iteminsta)
    return render_template(
        '/template.html',
	listagit=itemgit,
	listainsta=iteminsta,
    )

@app.route("/getlistagithub")
def listagit():
    listagit = os.listdir("./static/github")
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
