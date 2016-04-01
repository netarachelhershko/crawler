from datetime import datetime
from db_manager import DBManager
from url_scanner import UrlScanner
from utils import get_same_domain_urls, get_external_urls, get_domain


class Crawler(object):
    """ Crawler - a simple web-crawler that follows internal
        and external links.
        It will save all its results in a DB, and will go on till it get to a defined max depth.
    """

    def __init__(self, db_file='crawler.db'):
        """
        :param db_file: The database file name to be saved
        """
        self._url_scanner = UrlScanner()
        self._db_manager = DBManager(db_file)
        self._internal_urls_to_scan = []
        self._external_urls_to_scan = []
        self._max_page_depth = None
        self._max_external_sites_page_depth = None
        self._domain = None

    def crawl(self, url, max_page_depth=5, max_external_sites_page_depth=4, request_rate_limit=4):
        """
        Will crawl a given url up to max_page_depth and max_external_sites_page_depth on a max rate of
        request_rate_limit.
        :param url: The to-be crawled url
        :param max_page_depth: Max internal (same-domain) depth
        :param max_external_sites_page_depth: Max external (different-domain) depth
        :param request_rate_limit: Up to n requests at once
        :return: List of Url objects (See schemas/url.py)
        """
        self._url_scanner.set_request_limit(request_rate_limit)
        self._max_page_depth = max_page_depth
        self._max_external_sites_page_depth = max_external_sites_page_depth
        self._domain = get_domain(url)

        self._internal_urls_to_scan.append(url)
        self._crawl_internal_urls()
        self._crawl_external_urls()
        return self._get_crawled_urls()

    def _get_crawled_urls(self):
        return self._db_manager.get_crawled_urls()

    def _crawl_internal_urls(self):
        while self._internal_urls_to_scan and self._max_page_depth:
            child_urls = self._url_scanner.scan(self._internal_urls_to_scan)
            child_urls = list(set(child_urls) - set([x.url for x in self._db_manager.get_crawled_urls()]))
            self._internal_urls_to_scan = get_same_domain_urls(self._domain, child_urls)
            self._external_urls_to_scan.extend(get_external_urls(self._domain, child_urls))
            url_objects = [{'url': url, 'crawl_time': datetime.now()} for url in self._internal_urls_to_scan]
            self._db_manager.update(url_objects)
            self._max_page_depth -= 1

    def _crawl_external_urls(self):
        while self._external_urls_to_scan and self._max_external_sites_page_depth:
            self._external_urls_to_scan = self._url_scanner.scan(self._external_urls_to_scan)
            self._external_urls_to_scan = list(
                set(self._external_urls_to_scan) - set([x.url for x in self._db_manager.get_crawled_urls()]))
            url_objects = [{'url': url, 'crawl_time': datetime.now()} for url in self._external_urls_to_scan]
            self._db_manager.update(url_objects)
            self._max_external_sites_page_depth -= 1
