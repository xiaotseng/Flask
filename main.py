<<<<<<< HEAD
from flask import Flask, make_response, render_template, request
from flask_bootstrap import Bootstrap

=======
#encoding: utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from views import view
>>>>>>> 98d6177a93bf6421a890db09a7400f4f85e39fa8
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kfeefeuplkmmnkl'
bootstrap = Bootstrap(app)
<<<<<<< HEAD


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


=======
view(app)#注册函数
>>>>>>> 98d6177a93bf6421a890db09a7400f4f85e39fa8
if __name__ == "__main__":
    app.run(debug=True)
