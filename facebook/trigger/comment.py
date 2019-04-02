from facebook.utils import constants
import json
import logging

FACEBOOK_VERSION = "v3.2"
FECTH_FACEBOOK_COMMENT_URL = "https://graph.facebook.com/%s/%s_%s/comments?fields=from,parent&&summary=1&filter=stream&order=reverse_chronological&access_token=%s&limit=1&pretty=1"


def fetch_facebook_comment(page_id, post_id, page_access_token):
    try:
        return constants.get_network_instance().process_get(FECTH_FACEBOOK_COMMENT_URL % (FACEBOOK_VERSION, page_id, post_id, page_access_token))
    except Exception:
        raise Exception("Cannot get comment of %s on page: %s" % (post_id, page_id))


def process_facebook_comments(page_id, post_id, page_access_token):
    '''
    Process fetching comments from facebook

    :param page_id: page id
    :param post_id:  post id
    :param page_access_token: page token
    :return: None
    '''
    comments_json = json.loads(fetch_facebook_comment(page_id, post_id, page_access_token))
    next_paging = None
    has_paging = False
    if "paging" in comments_json:
        if "next" in comments_json["paging"]:
            has_paging = True
            next_paging = comments_json["paging"]["next"]
    if has_paging:
        process_facebook_comments_iterator(comments_json["data"], next_paging)
    else:
        process_facebook_comments_iterator(comments_json["data"], None)


def process_facebook_comments_iterator(json_object_data, next_url=None):
    '''
    Process one page of comment data. In case of having paging, process next page
    :param json_object_data: current comment facebook data
    :param next_url: next cursor
    :return:
    '''
    process_facebook_comment_data(json_object_data)
    if next_url:
        next_comments_json = json.loads(constants.get_network_instance().process_get(next_url))
        next_paging = None
        has_paging = False
        if "paging" in next_comments_json:
            if "next" in next_comments_json["paging"]:
                has_paging = True
                next_paging = next_comments_json["paging"]["next"]
        if has_paging:
            if "data" in next_comments_json:
                process_facebook_comments_iterator(next_comments_json["data"],next_paging)
        else:
            if "data" in next_comments_json:
                process_facebook_comments_iterator(next_comments_json["data"],None)



def process_facebook_comment_data(json_object_data):
    '''
    Process facebook comment data
    :param json_object_data: json data
    :return:  None
    '''
    for comments in json_object_data:
        logging.warning(comments["id"])
