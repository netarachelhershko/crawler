from html_url_extractor import HtmlUrlExtractor
from test_base import TestBase


class HtmlUrlExtractorTests(TestBase):
    def setUp(self):
        self._html_url_extractor = HtmlUrlExtractor()

    def test_extract_sanity(self):
        extracted = self._html_url_extractor.extract_from(open('html_templates/a.html').read(), include_nofollow=False)
        expected = ['http://example.com/b.html', 'http://example.com/c.html']
        self.assertListEqual(extracted, expected)
