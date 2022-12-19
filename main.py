import time

import praw

from config import *

reddit = praw.Reddit(
    user_agent = USER_AGENT,
    client_id = CLIENT_ID,
    client_secret = CLIENT_SECRET,
    username = REDDIT_USERNAME,
    password = REDDIT_PASSWORD
)
redditor = reddit.redditor(USER)

prev_comments = [i.id for i in redditor.comments.new(limit=10)]
prev_posts    = [i.id for i in redditor.submissions.new(limit=10)]

while True:
    try:
        new_comments = [i.id for i in redditor.comments.new(limit=10)]
        if prev_comments != new_comments:
            prev_comments = new_comments
            praw.models.Comment(reddit, id=new_comments[0]).reply(REPLY_TEXT)

        new_posts = [i.id for i in redditor.submissions.new(limit=10)]
        if prev_posts != new_posts:
            prev_posts = new_posts
            praw.models.Submission(reddit, id=new_posts[0]).reply(REPLY_TEXT)
    except Exception as e:
        print(f"Unhandled exception: {e}")
        
    time.sleep(WAIT_TIME)