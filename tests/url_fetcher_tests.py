from mocks.url_fetcher_mocks import get_url_fetcher_mock
from test_base import TestBase


class UrlFetcherTests(TestBase):
    def setUp(self):
        request_limit = 4
        self.url_fetcher = get_url_fetcher_mock(request_limit)

    def test_fetch_sanity(self):
        fetched = self.url_fetcher.fetch_from(['http://example.com/a.html'])
        expected = ['http://example.com/b.html', 'http://example.com/c.html', 'http://example.com/from_sitemap.html']
        self.assertSequenceEqual(fetched, expected)
