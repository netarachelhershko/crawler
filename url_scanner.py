from robots_validator import RobotsValidator
from reppy.cache import RobotsCache
from url_fetcher import UrlFetcher


class UrlScanner(object):
    """ Scan a url for child urls """

    def __init__(self, request_rate_limit=10):
        self.robots = RobotsCache()
        self.url_fetcher = UrlFetcher(request_rate_limit)
        self.robots_validator = RobotsValidator(agent='*')

    def set_request_limit(self, request_rate_limit):
        self.url_fetcher.set_request_limit(request_rate_limit)

    def scan(self, urls):
        """
        :param urls: A list of urls to scan child urls of
        :return: A list of robots.txt allowed child urls found within given urls
        """
        child_urls = self.url_fetcher.fetch_from(urls)
        relevant_child_urls = self.robots_validator.get_allowed_from(child_urls)
        return relevant_child_urls
