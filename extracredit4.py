import praw
import random
import time

reddit = praw.Reddit('bot')

for submission in reddit.subreddit('Liberal').hot(limit=None): 
    submission = random.choice(list(reddit.subreddit('Liberal').hot(limit=None)))
    title = submission.title
    url = submission.url
    print('title of the submission=', submission.title)
    submission_url = 'https://old.reddit.com/r/BotTown2/'
    reddit.subreddit("BotTown2").submit(title, url=submission.url)
    time.sleep(15)


selftext = "Everyone should support Bernie Sanders"
reddit.subreddit("BotTown2").submit("Bernie is Cool", selftext)

selftext = "Bernie Sanders is the best candidate for president"
reddit.subreddit("BotTown2").submit("Bernie is the best", selftext)

selftext = "Vote for Bernie!"
reddit.subreddit("BotTown2").submit("Feel the Bern", selftext)


