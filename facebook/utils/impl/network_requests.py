from ..inetwork import HttpUtil
import requests
import logging


class HttpUtilsRequest(HttpUtil):
    @staticmethod
    def process_get(url):
        if not url or not url.strip():
            logging.warning("URL is empty")
            return None
        http_response = requests.get(url)
        if http_response.status_code != requests.codes.ok:
            raise Exception("Request is not successful " + url)
        return http_response.content

    def process_post(url, url_params):
        pass