from database import Base
from sqlalchemy import Column,Integer,String ,TIMESTAMP,Boolean,text
class url(Base):
    __tablename__ =  "Url"
    id = Column(Integer,primary_key=True)
    url_link = Column(String,nullable = False,unique = True)
    subtitles = Column(String,default = "no subtitles") 
       