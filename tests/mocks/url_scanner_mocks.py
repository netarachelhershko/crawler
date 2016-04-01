from url_fetcher_mocks import get_url_fetcher_mock
from robots_validator import RobotsValidator
from reppy.cache import RobotsCache
from url_scanner import UrlScanner
from mock import MagicMock


def get_scanner_mock(request_limit):
    robots_cache = RobotsCache()
    robots_cache.fetch = MagicMock(return_value=robots_cache)
    robots_cache.allowed = MagicMock(return_value=True)
    robots_validator = RobotsValidator(agent='*')
    robots_validator.robots = robots_cache
    scanner = UrlScanner(request_limit)
    scanner.url_fetcher = get_url_fetcher_mock(request_limit)
    scanner.robots_validator = robots_validator
    return scanner
