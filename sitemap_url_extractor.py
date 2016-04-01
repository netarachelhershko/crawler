from BeautifulSoup import BeautifulSoup


class SitemapUrlExtractor(object):
    """ Extracts all urls from a sitemap (xhtml type) """

    def extract_from(self, sitemap):
        try:
            soup = BeautifulSoup(sitemap)
            locations = soup.findAll('loc')
            return [x.text for x in locations]
        except:
            return []
