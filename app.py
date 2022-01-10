from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('addUser.html')




@app.route("/addUser", methods=["POST"])
def addUser():


    id = request.form['id']
    pw = request.form['pw']
    nickname = request.form['nickname']

    if (id == "" or pw == "" or nickname == ""):
        return jsonify({'result': 'fail', 'msg': 'please check input'});
    doc = {
        'id': id,
        'pw': pw,
        'nickname': nickname,

    }
    db.user.insert_one(doc);
    return jsonify({'msg': "입력."});

    if db.users.find_one({'id': id}) == True:
        return jsonify({'msg': "이미 존재하는 아이디입니다."})
    else:
        return jsonify({'msg': "가입 가능한 아이디입니다"})

    if (result == False):
        return jsonify({'result': 'fail'});
    else:
        return jsonify({'result': 'success'});



#
# @app.route("/deleteUser", methods=["POST"])
# def deleteUser():
#     id = request.form['id']
#     db.deleteUser(id)
#     return jsonify({'result': 'success'});


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)