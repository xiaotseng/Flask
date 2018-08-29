from flask import make_response, render_template, request,redirect,url_for,session,g
from werkzeug.utils import secure_filename
import datetime
import os
def view(app):
    #第一次请求
    @app.before_first_request
    def before_first_request():
        pass

    @app.before_request
    def before_request():
        g.current_time=datetime.datetime.utcnow()
        print("请求")

    #没有找到页面
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
        

    #服务器错误
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500


    #首页
    @app.route("/")
    def index():
        return render_template("index.html")

    #用户测试
    @app.route("/user/<name>")
    def user(name):
        return render_template("user.html", name=name)

    #上传
    @app.route("/upload",methods=['POST','GET'])
    def upload():
        if request.method=='POST':
            f=request.files.get("file",None)
            if f==None:
                session["result"]="file null"
                return redirect(url_for('upload'))
            else:
                filename=f.filename
                basepath=os.path.dirname(__file__)#当前文件目录
                upload_path=os.path.join(basepath,'uploads',secure_filename(filename))
                f.save(upload_path)
                session["result"]="succeed"
                return redirect(url_for('upload'))     
        result=session.get("result","blank")#读取
        session["result"]="blank"#重置
        return render_template('upload.html',result=result)
    return app


