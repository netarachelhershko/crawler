from request_getter_mocks import get_request_getter_mock
from sitemap_fetcher import SitemapFetcher
from mock import MagicMock


def get_sitemap_fetcher_mock(request_limit):
    fetcher = SitemapFetcher(request_limit=request_limit)
    fetcher._try_fetch_sitemaps = MagicMock(return_value={'http://example.com': ['http://example.com/sitemap.xml']})
    fetcher.requests_getter = get_request_getter_mock(request_limit)
    return fetcher
