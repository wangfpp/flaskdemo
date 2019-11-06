# !/usr/bin/python3
# -*- coding: utf-8 -*-
## 运行项目

from flask import Flask, render_template, request

app = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="web")
@app.route('/')

def index():
    return render_template('index.html', name="wangfpp")

@app.route('/list', methods=['GET', 'POST'])
def list_name():
    method = request.method
    selectitem = 'app'
    lista= ["app", "Python", "Electron", "Shell"]
    if method == 'GET':
        return render_template('list.html', title="列表循环", list=lista, curr=selectitem)
    elif method == 'POST':
        req_dict = request.form.to_dict()
        print(req_dict["name"])
        return render_template('list.html', title="列表循环", list=lista, curr=req_dict["name"])
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8088)