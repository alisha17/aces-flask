from app import app
from app.model import Users, Messages
from flask import request, jsonify, session


@app.route('/login', methods=['POST'])
def login():
    response = dict()
    request_data = request.get_json(silent=True, force=True)
    user = Users.objects(username=request_data.get('username'), password=request_data.get('password'))
    session[request_data.get('username')] = True
    print(session)
    if bool(user):
        response["message"] = "logged_in"
        return jsonify(response)
    else:
        response["message"] = "User not found"
        return jsonify(response)


@app.route('/logout/<username>', methods=['GET'])
def logout(username):
    response = dict()
    session[username] = False
    response["message"] = "logged out"
    return jsonify(response)


@app.route('/create', methods=['POST'])
def create():
    response = dict()
    request_data = request.get_json(silent=True, force=True)
    try:
        user = Users(username=request_data.get('username'), password=request_data.get('password')).save()
        response["message"] = "User created"
        return jsonify(response)
    except:
        response["message"] = "User not created"
        return jsonify(response)


@app.route('/messages/<username>', methods=['POST'])
def messages(username):
    response = dict()
    request_data = request.get_json(silent=True, force=True)
    if session.get(username):
        try:
            Messages.objects.get(username=username).update(push__messages=request_data.get('message'))
            response["message"] = "recorded new message"
            return jsonify(response)
        except Exception as e:
            Messages(username=username, messages=[request_data.get('message')]).save()
            response["message"] = "recorded new message"
            return jsonify(response)
    else:
        response["message"] = "User not logged in"
        return jsonify(response)


@app.route('/messages/<username>', methods=['GET'])
def listmessages(username):
    response = dict()
    print(session.get(username))

    if session.get(username):
        print("dndnndndnd")
        user = Messages.objects.get(username=username)
        if bool(user):
            response["data"] = user.messages
            return "User logged in"
    else:
        print("in else")
        response["message"] = "User not logged in"
        return jsonify(response)