from html_url_extractor import HtmlUrlExtractor
from request_getter import RequestGetter
from sitemap_fetcher import SitemapFetcher
from urlparse import urljoin


class UrlFetcher(object):
    """ Handles url fetching from both html source and sitemaps """
    def __init__(self, request_limit=10):
        self.html_url_extractor = HtmlUrlExtractor()
        self.sitemap_fetcher = SitemapFetcher(request_limit)
        self.requests_getter = RequestGetter(request_limit)

    def set_request_limit(self, request_rate_limit):
        self.sitemap_fetcher.set_request_limit(request_rate_limit)
        self.requests_getter.set_request_limit(request_rate_limit)

    def fetch_from(self, urls):
        """
        :param urls: A list of urls to fetch all child urls from
        :return: A list of child urls found within html source and sitemaps
        """
        children = self._get_html_urls(urls)
        urls_from_sitemap = self.sitemap_fetcher.fetch_from(urls)
        children.extend(urls_from_sitemap)
        return children

    def _get_html_urls(self, urls):
        html_contents = self.requests_getter.get_content_from(urls)
        results = []
        for url, content in zip(urls, html_contents):
            results.extend([urljoin(url, child) for child in
                           self.html_url_extractor.extract_from(content, include_nofollow=False)])
        return results
