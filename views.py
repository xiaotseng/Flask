#encoding: utf-8
import datetime
import json
import os

from flask import (Response, g, make_response, redirect, render_template,
                   request, session, url_for)
from werkzeug.utils import secure_filename

from appCreator import app


def addToFrontPage(displayName):
    def wrapper(func):
        def inwrapper(*args, **kwargs):#真实执行
            print("装饰器")
            return func(*args, **kwargs)
        return inwrapper
    return wrapper

#放抬头的页面
frontPageDic={"首页":"/","上传":"/upload","WebSocket":"/websocket"}
#设置路由
def view(app):
    # 第一次请求
    @app.before_first_request
    def before_first_request():
        pass

    @app.before_request
    def before_request():
        g.frontPageList=frontPageDic
        g.current_time = datetime.datetime.utcnow()
        print("有请求")

    # 没有找到页面
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    # 服务器错误

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    # 首页
    @app.route("/")
    def index():
        return render_template("index.html")

    # 用户测试
    @app.route("/user/<name>")
    def user(name):
        return render_template("user.html", name=name)

    # 上传
    @app.route("/upload", methods=['POST', 'GET'])
    #@addToFrontPage("上传")
    def upload():
        if request.method == 'POST':
            f = request.files.get("file", None)
            if f == None:
                session["result"] = "file null"
                return redirect(url_for('upload'))
            else:
                filename = f.filename
                basepath = os.path.dirname(__file__)  # 当前文件目录
                upload_path = os.path.join(
                    basepath, 'uploads', secure_filename(filename))
                f.save(upload_path)
                session["result"] = "succeed"
                return redirect(url_for('upload'))
        result = session.get("result", "blank")  # 读取
        session["result"] = "blank"  # 重置
        return render_template('upload.html', result=result)


    # AJAX请求/////////////////////////////
    @app.route("/getjson", methods=['POST', 'GET'])
    def returnJson():
        requestData = json.loads(request.data.decode())
        print("GetJsonRequst:", requestData["name"])
        return "你好"+requestData["name"]

    #websocket测试页面
    @app.route('/websocket')
    def websocket():
        return render_template("WebSocketTest.html")
        pass
    return app

if __name__=="__main__":
    pass
else:
    print("引入%s模块" % __name__)
