from urlparse import urlparse
from tld import get_tld

from BeautifulSoup import BeautifulSoup


class HtmlUrlExtractor(object):
    """ Extracts urls from given html source """

    def extract_from(self, html, include_nofollow):
        """
        :param html: Html source
        :param include_nofollow: If false then excludes nofollow links
        :return: A list of urls found within html source
        """
        try:
            soup = BeautifulSoup(html)
            hrefs = [a['href'] for a in soup.findAll('a', href=True) if
                     urlparse(a['href']).netloc and get_tld(a['href'], fail_silently=True)]
            if not include_nofollow:
                nofollow = [a['href'] for a in soup.findAll('a', {"rel": "nofollow"}, href=True)]
                hrefs = list(set(hrefs) - set(nofollow))
            return hrefs
        except:
            return []
