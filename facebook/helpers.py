from facebook.utils import constants
import json

FACEBOOK_VERSION = "v3.2"
FECTH_FACEBOOK_ME_URL = "https://graph.facebook.com/%s/me?access_token=%s"


def get_page_id_from_page_access(page_access_token):
    try:
        response = constants.get_network_instance().process_get(FECTH_FACEBOOK_ME_URL % (FACEBOOK_VERSION, page_access_token))
        response_object = json.loads(response)
        if not response_object["id"]:
            raise Exception("Cannot get me  from page_access" % page_access_token)
        return response_object["id"]
    except Exception:
        raise Exception("Cannot get me  from page_acess" % page_access_token)

