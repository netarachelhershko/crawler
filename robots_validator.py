from reppy.cache import RobotsCache
from utils import get_domain


class RobotsValidator(object):
    """ Validates urls via robots.txt file """
    def __init__(self, agent):
        self._agent = agent
        self.robots = RobotsCache()

    def get_allowed_from(self, child_urls):
        """
        :param child_urls: List of child urls to check robots.txt on
        :return: A list of allowed child urls to crawl
        """
        allowed = []
        domains = list(set('{0}'.format(get_domain(url)) for url in child_urls))
        domain_to_children = {domain: filter(lambda u: get_domain(u) == domain, child_urls) for domain in domains}
        for domain in domain_to_children:
            try:
                rules = self.robots.fetch(domain)
                for url in domain_to_children[domain]:
                    if rules.allowed(url, self._agent):
                        allowed.append(url)
            except:
                allowed.extend(domain_to_children[domain])
        return allowed
