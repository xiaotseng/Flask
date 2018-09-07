from flask_login import LoginManager

from appCreator import app

#登陆管理器
loginmanager=LoginManager(app)
loginmanager.session_protection='strong'
loginmanager.login_view='main.login'
loginmanager.init_app(app)

@loginmanager.user_loader
def load_user(id):
    return
