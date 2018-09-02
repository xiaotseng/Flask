#encoding: utf-8
import sys
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from views import view

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kfeefeuplkmmnkl'
bootstrap = Bootstrap(app)
moment=Moment(app)
view(app)#注册函数
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
