import abc


class HttpUtil(abc.ABC) :
    @abc.abstractmethod
    def process_get(url):
        pass

    @abc.abstractmethod
    def process_post(url, url_params):
        pass
