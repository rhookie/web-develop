from flask_sqlalchemy import SQLAlchemy

class PasteFile:
    __tablename__="PasteFile"
    db=SQLAlchemy()
    id=db.Column(db.Integer,primary_key=True)
    filename=db.Column(db.String(5000),nullable=False)
    filehash=db.Column(db.String(128),nullable=False,unique=True)
    filemd5=db.Column(db.String(128),nullable=False,unique=True)
    