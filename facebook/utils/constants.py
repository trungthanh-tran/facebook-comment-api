from .impl.network_requests import HttpUtilsRequest


def get_network_instance():
    return HttpUtilsRequest()