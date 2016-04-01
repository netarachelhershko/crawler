from urlparse import urlparse


def get_same_domain_urls(domain, children):
    """
    :param domain: A domain of type {scheme}://{netloc}
    :param children: Child urls found in domain
    :return: A list of all child urls that are part of given domain
    """
    results = [u for u in children if domain == get_domain(u)]
    return results


def get_external_urls(domain, children):
    """
    :param domain: A domain of type {scheme}://{netloc}
    :param children: Child urls found in domain
    :return: A list of all child urls that are not part of a given domain
    """
    internal = get_same_domain_urls(domain, children)
    results = list(set(children) - set(internal))
    return results


def get_domain(url):
    """
    :param url: Any url
    :return: A domain of type {scheme}://{netloc}.
    For example: http://example.com/a.html -> http://example.com
    """
    return '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))


def is_url_valid(url):
    """
    :param url: Any url
    :return: True if valid, False if not
    """
    parsed = urlparse(url)
    return parsed.scheme and parsed.netloc
