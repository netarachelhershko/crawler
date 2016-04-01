from schemas.url import Url, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBManager(object):
    """ Managed the db session """
    def __init__(self, db_file):
        """
        :param db_file: Database file to open
        """
        self.engine = create_engine('sqlite:///{db}'.format(db=db_file))
        self.conn = self.engine.connect()
        self.session = sessionmaker(bind=self.engine)()
        self._create_tables()

    def update(self, url_objects):
        """
        Updates the database and commits results
        :param url_objects: List of Url objects (See schemas/url.py)
        """
        try:
            for url_obj in url_objects:
                url_obj = Url(url_obj['url'], url_obj['crawl_time'])
                self.session.add(url_obj)
            self.session.commit()
        except:
            pass

    def get_crawled_urls(self):
        return self.session.query(Url).all()

    def _create_tables(self):
        Base.metadata.create_all(self.engine)
