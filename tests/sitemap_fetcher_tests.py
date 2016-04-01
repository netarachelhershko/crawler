from mocks.sitemap_fetcher_mocks import get_sitemap_fetcher_mock
from test_base import TestBase


class SitemapFetcherTests(TestBase):
    def setUp(self):
        request_limit = 4
        self.sitemap_fetcher = get_sitemap_fetcher_mock(request_limit)

    def test_fetch_sanity(self):
        urls = self.sitemap_fetcher.fetch_from(['http://example.com/a.html'])
        expected = ['http://example.com/from_sitemap.html']
        self.assertListEqual(urls, expected)
