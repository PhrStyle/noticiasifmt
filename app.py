from flask import Flask, render_template
import os
import json

app = Flask(__name__)
app.debug = True
@app.route("/")
def mainpage():
    return render_template(
        '/template.html',
    )

@app.route("/getlista")
def lista():
    lista = os.listdir("./github")
    del lista[0]
    return json.dumps(lista)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
