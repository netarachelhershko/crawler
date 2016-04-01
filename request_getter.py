import grequests


class RequestGetter(object):
    """ Handles parallel requests with grequests """

    def __init__(self, request_limit=10):
        self.request_limit = request_limit

    def set_request_limit(self, request_rate_limit):
        self.request_limit = request_rate_limit

    def get_content_from(self, urls):
        """
        Gets urls with up to request_limit at once
        :param urls: List of urls
        :return: List of url contents (similar output to requests.get(url).content)
        """
        results = []
        urls_wrapped = [grequests.get(url) for url in urls]
        while urls_wrapped:
            results.extend([r.content for r in grequests.map(urls_wrapped[:self.request_limit],
                                                             exception_handler=RequestGetter._exception_handler) if r])
            urls_wrapped = urls_wrapped[self.request_limit:]
        return results

    @staticmethod
    def _exception_handler(request, exception):
        pass
