import os

import datetime
from django.shortcuts import redirect
from flask import Flask, render_template, redirect, jsonify, request, url_for, session
from flask_socketio import SocketIO, emit, send
from flask_session import Session
from channels import Channel
import urllib.request

APP_SECRET = 'set APP_SECRET=abc'
os.system(APP_SECRET)
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
socketio = SocketIO(app)
Session(app)
channels = []

#----KEYS-Remove after debugging----

#level0 - ewgv43235vd2r@#1fwe
#level1 - en1-ctfbox-app
#level2 - 3yudwdw1za#q#pghsl
#level3 - fdgwgqpodf13#$poqvm0
#level4 - fddehh#xraw45345ef4rfg
#level5 - bypass using /fakeLogin
#level6 - pewo2r#1dfffqrte0op
#level7 - 8ofefef2#o0p$fklfuewfjv
#level8 - TEST_AP
#level9 - F78A7C524F6205528BC331081F
#level10 - bypass using /remoteAccess --> trigger to the next level is not implemented
#level11 - 531203230
#level12 - sanvirafgergrguwurfreiii23
#level13 - SuperSecretPassword
#level14 - username -Alpha / password - @AlphaSearch
#level15 - 192168105

#-----------------------------------

@app.route("/")
def index():
        return render_template("welcome.html")

@app.route("/invalid")
def invalid():
        return render_template("invalid.html")

@app.errorhandler(404)
def page_not_found(e):
    if 'fakeLogin' in request.url:
       return "Key- pewo2r#1dfffqrte0op: " + request.path


@app.route("/chat", methods=["POST"])
def chat():
  key8 = request.form.get("key")
  if (key8) == 'F78A7C524F6205528BC331081F':
    try:
        return render_template("index.html", name=session["name"], lastChannel=session["lastChannel"], channels=channels)
    except KeyError:
        try:
            return render_template("index.html", name=session["name"], channels=channels)
        except KeyError:
            return render_template("index.html", channels=channels)

@app.route("/sheepsProfile%id=10003455%file=info.txt", methods=["POST"])
def profile():
        key = request.form.get("key")
        if (key) == 'ewgv43235vd2r@#1fwe':
            return render_template("sheepProfile.html")
        else:
            response = redirect('/invalid')
            return response

@app.route("/sheepsProfile%id=10003455%file=info.plist")
def profile1():
            return render_template("sheepProfile1.html")

@app.route("/Success", methods=["POST"])
def success():
    key0 = request.form.get("key")
    if (key0) == 'pewo2r#1dfffqrte0op':
            return render_template("success.html")
    else:
        response = redirect('/invalid')
        return response

@app.route("/viewsas", methods=["POST"])
def viewsas():

       key1 = request.form.get("key")
       if (key1) == 'en1-ctfbox-app':
            return render_template("viewsas.html")
       else:
            response = redirect('/invalid')
            return response

@app.route("/alphasProfile", methods=["POST"])
def alphasProfile():

       key2 = request.form.get("key")
       if (key2) == '3yudwdw1za#q#pghsl':
           return render_template("alphasProfile.html")
       else:
               response = redirect('/invalid')
               return response

@app.route("/profileContent", methods=["POST"])
def profileContent():

       content = "key-fddehh#xraw45345ef4rfg"
       key3 = request.form.get("key")
       if (key3) == 'fdgwgqpodf13#$poqvm0':
           return render_template("profileContent.html", content=content)
       else:
           response = redirect('/invalid')
           return response

@app.route("/youMissedIt")
def youMissedIt():
           return render_template("youMissedIt.html")

@app.route("/yourWishIsMyCommand", methods=["POST"])
def yourWishIsMyCommand():

       key6 = request.form.get("key")
       if (key6) == 'fddehh#xraw45345ef4rfg':
           return render_template("yourWishIsMyCommand.html")
       else:
           response = redirect('/invalid')
           return response

@app.route("/fakeLogin")
def fakeLogin():
           secretKey = "abc"
           return render_template("fakeLogin.html", secretKey=secretKey)

@app.route("/HiddenNetwork", methods=["POST"])
def hiddenwifi():

      key7 = request.form.get("key")
      if (key7) == '8ofefef2#o0p$fklfuewfjv':
            return render_template("hiddenwifi.html")
      else:
           response = redirect('/invalid')
           return response

@app.route("/HiddenNetworkpass", methods=["POST"])
def hiddenwifipass():
    key7 = request.form.get("key")
    if (key7) == 'TEST_AP':
            return render_template("hiddenwifipass.html")
    else:
        response = redirect('/invalid')
        return response

@app.route("/alphaProfileviewas")
def alphaProfileviewas():
        return render_template("alphaProfile1.html")

@app.route("/alphasProfile1")
def alphasProfile1():
        return render_template("alphasProfile1.html")

@app.route("/remoteAccess")
def remoteAccess():
            return render_template("remoteAccess.html")

@app.route("/binary", methods=["POST"])
def binary():
       key = request.form.get("key")
       if (key) == 'SuperSecretPassword':
            return render_template("binary.html")
       else:
           response = redirect('/invalid')
           return response

@app.route("/privilage", methods=["POST"])
def privilage():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Alpha' or request.form['password'] != '@AlphaSearch':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template("privilage.html")

    return render_template("binary.html", error=error)

@app.route("/name", methods=["POST"])
def name():
    name = request.form.get("name")
    if name is not '':
        session["name"] = name
        return jsonify({"success": True, "name": name})
    else:
        return jsonify({"success": False})

@app.route("/lastChannel", methods=["POST"])
def lastChannel():
    channel = request.form.get("lastChannel")
    session["lastChannel"] = channel
    return ''

@app.route("/channel", methods=["POST"])
def channel():
    channel = request.form.get('channel')
    for elem in channels:
        if channel in elem.name:
            return jsonify({"success": False})
    newChannel = Channel(channel)
    channels.append(newChannel)
    channelsFeed = []
    for object in channels:
        channelsFeed.append(object.__dict__)
    return jsonify({"success": True, "channel": channel, "channels": channelsFeed})

@app.route("/trace", methods=["POST"])
def trace():
    key7 = request.form.get("key")
    if (key7) == '531203230':
            return render_template("trace.html")
    else:
        response = redirect('/invalid')
        return response

@app.route("/pasteboard", methods=["POST"])
def pasteboard():
    key13 = request.form.get("key")
    if (key13) == 'sanvirafgergrguwurfreiii23':
            return render_template("pasteboard.html")
    else:
        response = redirect('/invalid')
        return response

@app.route("/crown", methods=["POST"])
def crown():
    key13 = request.form.get("key")
    if (key13) == '192168105':
            return render_template("crown.html")
    else:
        response = redirect('/invalid')
        return response

@socketio.on("sendMessage")
def chat(data):
    channel = data["channel"]
    message = data["message"]
    # Check all existing channels seeking for the same name
    for checkChannel in channels:
        # If exist then append the new message else emit a Not success message
        if checkChannel.name == channel:
            time = '{:%H:%M:%S}'.format(datetime.datetime.now())
            sender = session["name"]
            checkChannel.newMessage(message, sender, channel, time)

            last_message = checkChannel.messages[-1]
            emit("update", last_message, broadcast=True)
            return
    emit("update", 'Not success', broadcast=True)

@socketio.on("update")
def conect(data):
    channel = data["channel"]
    #Checking for an existing channel with that same name
    for checkChannel in channels:
        # If exist, charge all old messages stored there and emit
        if checkChannel.name == channel:
            oldMessages = checkChannel.messages
            name = session["name"]
            emit("updateChat", (oldMessages, name), broadcast=True)
            return
    # Else, emit a notFound message
    emit("updateChat", 'notFound', broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
