from utils import is_url_valid
from crawler import Crawler
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='A simple python web crawler')
    parser.add_argument('url', metavar='url', type=str, help='Url to crawl.')
    parser.add_argument('--max_page_depth', dest='max_page_depth', type=int, default=5,
                        help='Maximum depth to crawl on a given url.')
    parser.add_argument('--max_external_sites_page_depth', dest='max_external_sites_page_depth', type=int, default=4,
                        help='Maximum external sites depth to crawl on a given url.')
    parser.add_argument('--request_rate_limit', dest='request_rate_limit', type=int, default=4,
                        help='Maximum requests at once.')
    parsed = parser.parse_args()
    if not is_url_valid(parsed.url):
        print 'Please enter a url in the following format: http://example.com/optional_query'
    else:
        return parsed


if __name__ == '__main__':
    args = parse_args()
    if args:
        Crawler().crawl(**args.__dict__)
