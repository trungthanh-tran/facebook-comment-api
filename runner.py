from facebook import helpers as facebook_utils
from facebook.trigger import comment as facebook_comment
import facebook.utils.setup as util
import json
import logging


PAGE_ACCESS_TOKEN = "" # Need to be filled
POST_ID="425985347973405" # Need to be filled
PAGE_ID = "325510481354226" #  page_id = facebook_utils.get_page_id_from_page_access(PAGE_ACCESS_TOKEN)

def main():
    util.setup_logging()
    # Use requests as http network

    facebook_comment.process_facebook_comments(PAGE_ID, POST_ID, PAGE_ACCESS_TOKEN)



if __name__ == '__main__':
    main()