from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .import db
from .import login_manager

class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) #외래키로 하나만 연결 가능 
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User %r>' % self.username

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref ='role', lazy='dynamic') #user table과 연결하는 부분 - relationship 테이블의 경우 backref를 통해 여러 테이블과 연관될 수 있음

    def __repr__(self):
        return '<Role %r>' % self.name

@login_manager.user_loader #사용자 로더 콜백함수 - 이 부분이 있어야 @login_requeired 사용가능
def load_user(user_id):
    return User.query.get(int(user_id))