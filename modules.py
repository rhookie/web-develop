from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
print 'So cool'

class PasteFile:
    __tablename__="PasteFile"
    db=SQLAlchemy()
    id=db.Column(db.Integer,primary_key=True)
    filename=db.Column(db.String(5000),nullable=False)
    filehash=db.Column(db.String(128),nullable=False,unique=True)
    filemd5=db.Column(db.String(128),nullable=False,unique=True)
    
    def __init__(self,filename="",mimetype='application/octet-stream',size=0,filehash=None,filemd5=None):
        self.uploadtime=datetime.now()
        self.mimetype=mimetype 
        self.size=size 
        self.filehash=filehash if filehash else self.hash_filename(filename)
        self.filemd5=filemd5 
        
        