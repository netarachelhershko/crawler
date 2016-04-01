from request_getter_mocks import get_request_getter_mock
from sitemap_fetcher_mocks import get_sitemap_fetcher_mock
from url_fetcher import UrlFetcher


def get_url_fetcher_mock(request_limit):
    url_fetcher = UrlFetcher(request_limit)
    url_fetcher.requests_getter = get_request_getter_mock(request_limit)
    url_fetcher.sitemap_fetcher = get_sitemap_fetcher_mock(request_limit)
    return url_fetcher

