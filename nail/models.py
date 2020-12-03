# cmd 창에서 db init 을 해주어야 임포트 가능
from nail import db

class thumbnail(db.Model):
    __table_name__='thumbnail'

    index = db.Column(db.Integer, primary_key=True)
    youtuber = db.Column(db.String(50),nullable=False)
    title = db.Column(db.String(200),nullable=False)
    views = db.Column(db.Integer(),nullable=False)
    subscriber = db.Column(db.Integer(),nullable=False)
    imgAdr = db.Column(db.String(200),nullable=False)
    category = db.Column(db.String(50),nullable=False)
    score = db.Column(db.Float(10),nullable=False)

