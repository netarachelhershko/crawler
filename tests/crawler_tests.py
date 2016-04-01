from mocks.url_scanner_mocks import get_scanner_mock
from test_base import TestBase
from crawler import Crawler


class CrawlerTests(TestBase):
    def setUp(self):
        self.crawler = Crawler(db_file='test.db')
        request_limit = 4
        self.crawler._url_scanner = get_scanner_mock(request_limit)

    def test_crawl_sanity(self):
        crawled = self.crawler.crawl('http://example.com/a.html')
        expected = self._db_manager.get_crawled_urls()
        for in_crawl, in_expected in zip(crawled, expected):
            self.assertEqual(in_crawl.url, in_expected.url)
            self.assertEqual(in_crawl.crawl_time, in_expected.crawl_time)
