from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class url(Base):
    __tablename__ = "Url"
    id = Column(Integer, primary_key=True)
    url_link = Column(String, nullable=False, unique=True)
    subtitles = Column(String, default="no subtitles")


class modelanswer(Base):
    __tablename__ = "summary"
    id = Column(String, primary_key=True)
    response = Column(String, nullable=False, unique=True)
    urlid = Column(Integer, ForeignKey(url.id, ondelete="CASCADE"), nullable=False)
