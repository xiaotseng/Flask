#encoding: utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from views import view
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kfeefeuplkmmnkl'
bootstrap = Bootstrap(app)
view(app)#注册函数
if __name__ == "__main__":
    app.run(debug=True)
