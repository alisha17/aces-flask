from app import app
from app.model import Users, Messages
from flask import request, jsonify, session, make_response
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)


@app.route("/login", methods=["POST"])
def login():
    request_data = request.get_json(silent=True, force=True)
    user = Users.objects(
        username=request_data.get("username"), password=request_data.get("password")
    )
    if bool(user):
        access_token = create_access_token(identity=request_data["username"])
        data = {"message": "logged_in", "access_token": access_token}
        resp = make_response(data, 200)
        after_request(resp)
        return resp
    else:
        resp = make_response({"message": "Wrong credentials"}, 400)
        return resp


@app.route("/logout/<username>", methods=["GET"])
@jwt_required
def logout(username):
    resp = make_response({"message": "logged out"})
    after_request(resp)
    return resp


# @app.route('/create', methods=['POST'])
# def create():
#     response = dict()
#     request_data = request.get_json(silent=True, force=True)
#     try:
#         user = Users(username=request_data.get('username'), password=request_data.get('password')).save()
#         response["message"] = "User created"
#         return jsonify(response)
#     except:
#         response["message"] = "User not created"
#         return jsonify(response)


@app.route("/messages/<username>", methods=["POST"])
@jwt_required
def messages(username):
    response = dict()
    request_data = request.get_json(silent=True, force=True)
    try:
        Messages.objects.get(username=username).update(
            push__messages=request_data.get("message")
        )
        res_message = "added new message"
    except Exception as e:
        Messages(username=username, messages=[request_data.get("message")]).save()
        res_message = "recorded new message"

    return make_response({"message": res_message})


@app.route("/messages/<username>", methods=["GET"])
@jwt_required
def listmessages(username):
    response = dict()
    user = Messages.objects.get(username=username)
    if bool(user):
        resp = make_response({"data": user.messages})
        after_request(resp)
        return resp
    else:
        return make_response("User doesn't exists!", 400)


def after_request(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Credentials"] = True
