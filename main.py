"""
by NayoBd
"""
from flask import Flask, render_template, session, redirect, url_for
import uuid

app = Flask("Unopoly")
app.config["SECRET_KEY"] = str(uuid.uuid4())
app.config.update(SESSION_COOKIE_SECURE=True, SESSION_COOKIE_SAMESITE="None")

# Page d'accueil


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Créer/Rejoindre une partie


@app.route("/play/", methods=["GET"])
def play():
    return render_template("play.html")

# Partie


@app.route("/play/<idParty>/", methods=["GET"])
def party(idParty):
    return render_template("party.html")

# Rejoindre par lien


@app.route("/join/<idParty>/", methods=["GET"])
def join(idParty):
    return redirect(url_for("index"))


app.run(port=8000, host="0.0.0.0", threaded=True, debug=True)
