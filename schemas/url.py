from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Url(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)
    crawl_time = Column(DateTime)

    def __init__(self, url, crawl_time):
        self.url = url
        self.crawl_time = crawl_time
