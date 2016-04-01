from db_manager import DBManager
from test_base import TestBase
from datetime import datetime


class DBManagerTests(TestBase):
    def setUp(self):
        self.db_manager = DBManager('test.db')

    def test_insertion_sanity(self):
        self.db_manager.update([
            {'url': 'http://example.com/', 'crawl_time': datetime.now()},
            {'url': 'http://example.com/a.html', 'crawl_time': datetime.now()}])
        crawled = self.db_manager.get_crawled_urls()
        expected = ['http://example.com/', 'http://example.com/a.html']
        self.assertEqual([x.url for x in crawled], expected)
