#encoding: utf-8
from flask import Flask

#实例一个Flask
app = Flask(__name__,static_folder="./static",template_folder="./templates")
#配置Flask
app.config['SECRET_KEY'] = 'kfeefeuplkmmnkl'#密钥
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://webUser:aaakkk@baoge.vip/webDatabase"
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] =True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

if __name__=="__main__":
    pass
else:
    print("引入%s模块" % __name__)
