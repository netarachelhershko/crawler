from sitemap_url_extractor import SitemapUrlExtractor
from request_getter import RequestGetter
from reppy.cache import RobotsCache
from utils import get_domain


class SitemapFetcher(object):
    """ Gets all urls found within a sitemap """
    def __init__(self, request_limit=10):
        self.sitemap_url_extractor = SitemapUrlExtractor()
        self.requests_getter = RequestGetter(request_limit)

    def set_request_limit(self, request_rate_limit):
        self.requests_getter.set_request_limit(request_rate_limit)

    def fetch_from(self, urls):
        """
        :param urls: A list of urls to fetch sitemaps of
        :return: A list of urls that was found within each sitemap of given urls
        """
        unique_domains = list(set(get_domain(u) for u in urls))
        sitemaps = self._try_fetch_sitemaps(unique_domains)
        results = []
        for url in sitemaps:
            sitemaps_content = self.requests_getter.get_content_from(sitemaps[url])
            for content in sitemaps_content:
                locations = self.sitemap_url_extractor.extract_from(content)
                locations = filter(lambda u: not u.endswith('.xml'), locations)
                results.extend(locations)
        return results

    def _try_fetch_sitemaps(self, urls):
        sitemaps = {}
        for url in urls:
            try:
                sitemaps[url] = self._fetch_sitemap_from_url(url)
            except:
                pass
        return sitemaps

    def _fetch_sitemap_from_url(self, url):
        robots = RobotsCache()
        try:
            return robots.fetch(url, timeout=1.5).sitemaps
        except:
            return []
