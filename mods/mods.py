#encoding: utf-8
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy, sqlalchemy

from appCreator import app

#数据库实例
db=SQLAlchemy(app)
class User(db.Model,UserMixin):
    #用户数据表类
    __tablename__="users"
    id=sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    username=sqlalchemy.Column(sqlalchemy.String(64),unique=True,index=True)
    role_id=sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.ForeignKey('roles.id'))
    hash_password=sqlalchemy.Column(sqlalchemy.String(28))

class Role(db.Model):
    #角色数据表类
    __tablename__="roles"
    id=sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name=sqlalchemy.Column(sqlalchemy.String(64),unique=True,index=True)
#创建数据库
#db.create_all()





if __name__=="__main__":
    pass
else:
    print("引入%s模块" % __name__)
