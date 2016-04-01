from request_getter import RequestGetter
from urlparse import urlparse
from os.path import join


def get_request_getter_mock(request_limit):
    request_getter = RequestGetter(request_limit)
    request_getter.get_content_from = lambda urls: [
        open(join('html_templates', '{url}'.format(url=urlparse(url).path[1:]))).read() for url in urls]
    return request_getter
