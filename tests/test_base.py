from db_manager import DBManager
from schemas.url import Url
import unittest


class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBase, self).__init__(*args, **kwargs)
        self._db_manager = DBManager('test.db')
        Url.__table__.drop(self._db_manager.engine)
        self._db_manager._create_tables()
