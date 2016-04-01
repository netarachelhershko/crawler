from mocks.url_scanner_mocks import get_scanner_mock
from test_base import TestBase


class UrlScannerTests(TestBase):
    def setUp(self):
        request_limit = 4
        self.url_scanner = get_scanner_mock(request_limit)

    def test_scan_sanity(self):
        url = 'http://example.com/a.html'
        results = self.url_scanner.scan([url])
        expected = ['http://example.com/b.html', 'http://example.com/c.html', 'http://example.com/from_sitemap.html']
        self.assertSequenceEqual(results, expected)
