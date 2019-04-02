# facebook-comment-api


This project implements the simplest way to fetch comments list from a facebook post and process it. To test, you need to prepare
- Facebook page access token: Grab at https://developers.facebook.com/tools/explorer/
- Post ID: Facebook ID of your post. You can grab in by using https://commentpicker.com/facebook-post-id-finder.php
- Page ID: Grab by https://graph.facebook.com/<version_facebook>/me?access_token=<Page access token above>

Requirements:
- Python3
- PIP

Setup env:
- pip install -r requirements.txt

Run:
- python runner.py

Feel free to use it