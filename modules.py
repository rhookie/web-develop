from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
import cropresize2
from PIL import Image 
import os 
from flask import abort 
import uuid 

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
        self.filehash=filehash if filehash else self._hash_filename(filename)
        self.filemd5=filemd5 
    
    @classmethod
    def rsize(cls,old_paste,weight,height):
        assert old_paste.is_image,TypeError('Unsupported Image Type.')
        img=cropresize2.crop_resize(Image.open(old_paste.path),(int(weight),int(height)))
        rst=cls(old_paste.filename,old_paste.mimetype,0)
        img.save(rst.path)
        filestate=os.stat(rst.path)
        rst.size=filestate.st_size 
        return rst 
    
    @classmethod 
    def get_by_filehash(cls,filehash,code=404):
        return cls.query.filter_by(filehash=filehash).first() or abort()
    
    @classmethod 
    def get_by_md5(cls,filemd5):
        return cls.query.filter_by(filemd5=filemd5).first() 
    
    @staticmethod
    def _hash_filename(filename):
        _,_,suffix=filename.rpartition('.')
        return '%s.%s'%(uuid.uuid4().hex,suffix)
    
    
        