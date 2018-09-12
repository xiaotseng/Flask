from flask_script import Shell,Manager
from threading import Thread
from mods import User,Role,db
db.make_connector()
from appCreator import app
manager=Manager(app)
def mak_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
manager.add_command("shell",Shell(make_context=mak_shell_context))
if __name__=="__main__":
    manager.run()