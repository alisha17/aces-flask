# from flask import Flask, request, jsonify
# from pymongo import *
from app import app
#
# app = Flask(__name__)
#
# client = MongoClient('localhost', 27017)
# db = client.aces

# class Users(Document):
#     username = StringField(max_length=60, required=True)
#     password = StringField(max_length=60, required=True)

# class Messages(Document):
#     username = StringField(max_length=60, required=True)
#     messages = ListField(StringField())


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = jsonify(request.json["username"])
#     password = jsonify(request.json["password"])
#
#     user_collection = db['users']
#
#     if user_collection.find({'username': username, 'password':password}).count() == 1:
#         blah = True
#     else:
#         blah = False
#     # Post.objects(Q(published=True) | Q(publish_date__lte=datetime.now()))
#
#     return "fff"


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=5000)
