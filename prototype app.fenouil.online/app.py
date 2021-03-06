from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def pagehome():
    return render_template("home.html", message_bienvenue="Bienvenue dans le système de saisie FENOUIL")

@app.route("/clients")
def pageclients():
    return render_template("page_clients.html")

@app.route("/article")
def pagearticle():
    return render_template("page_article.html")

@app.route("/statistiques")
def pagestatistiques():
    return render_template("page_statistiques.html")

if __name__ == '__main__':
    app.run()
