#encoding: utf-8
import sys

from flask_bootstrap import Bootstrap
from flask_moment import Moment

from appCreator import app
from controls import login
from views import view

bootstrap = Bootstrap(app)
moment=Moment(app)
view(app)#注册函数

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
