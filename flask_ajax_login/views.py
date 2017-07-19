#_*_ coding:utf-8 _*_
from flask import Flask,jsonify,request
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'nfkt123!' :
        return jsonify({'login_info': 'success'})
    else:
        return jsonify({'login_info': 'fail'})


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8080')