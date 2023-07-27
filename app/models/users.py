import bcrypt
from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean(), unique=False, default=False)
    created_at = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime, nullable=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, fname, lname, created_at):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.created_at = created_at

    def __repr__(self):
        return self.fname + ' ' + self.lname

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
