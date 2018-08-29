from flask import Flask, make_response, render_template, request,redirect,url_for,session
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from enum import Enum
import os
#class uploadResult(Enum):
    
app = Flask(__name__)
bootstrap = Bootstrap(app)

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
            return redirect(url_for('upload'))
        else:
            basepath=os.path.dirname(__file__)#当前文件目录
            upload_path=os.path.join(basepath,'uploads',secure_filename(f.filename))
            f.save(upload_path)
            return redirect(url_for('upload'))
    return render_template('upload.html')

#没有找到页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#服务器错误
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
