# !/usr/bin/python3
# -*- coding: utf-8 -*-
## 运行项目

from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="web")
UPLOAD_FOLDER = "upload"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
base_dir = os.path.abspath(os.path.dirname(__file__))

## 首页路由
@app.route('/')
def index():
    return render_template('index.html', name="wangfpp")

## 列表页路由
@app.route('/list', methods=['GET', 'POST'])
def list_name():
    method = request.method
    selectitem = 'app'
    lista= [{"title": 'app', "name": 'app', "desc": 'peoject', "childrens": []},
                 {"title": 'Vue', "name": 'Vue', "desc": '前端项目框架', "childrens": ['route', 'vuex']},
                 {"title": 'ReactNative', "name": 'ReactNative', "desc": '媲美原生应用的App框架', "childrens": ['JSBridge', 'Route', 'Storage']}]
    if method == 'GET':
        return render_template('list.html', title="列表循环", list=lista, curr=selectitem)
    elif method == 'POST':
        req_dict = request.form.to_dict()
        print(req_dict["name"])
        return render_template('list.html', title="列表循环", list=lista, curr=req_dict["name"])

## 上传文件
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file_dir = os.path.join(base_dir, app.config['UPLOAD_FOLDER'])
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        files_list = request.files.to_dict()
        for (key, f) in files_list.items():
            fname = secure_filename(f.filename)
            f.save(os.path.join(file_dir, f.filename))
        return render_template('upload.html')
    else:
        return render_template('upload.html', title="文件上传")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8088)