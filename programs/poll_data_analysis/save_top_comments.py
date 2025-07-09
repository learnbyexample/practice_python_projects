import json
import praw

with open('.secrets/tokens.json') as f:
    secrets = json.load(f)

reddit = praw.Reddit(
    user_agent=secrets['user_agent'],
    client_id=secrets['client_id'],
    client_secret=secrets['client_secret'],
)

thread_details = (('2019', 'cib77j'), ('2021', 'm20rd1'))

for year, thread_id in thread_details:
    submission = reddit.submission(id=thread_id)
    submission.comments.replace_more(limit=None)

    op_file = f'top_comments_{year}.txt'
    with open(op_file, 'w') as f:
        for top_level_comment in submission.comments:
            f.write(top_level_comment.body + '\n')

