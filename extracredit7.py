#EXTRA CREDIT 7 (both parts)

# Have your bot upvote any comment or submission that mentions your favorite candidate. 
# I recommend creating a separate python file for performing the upvotes, 
# and you must be able to upvote comments contained within any submission in the class subreddit.

# You may earn an additional two points if you use the TextBlob sentiment analysis library to 
# determine the sentiment of all the posts that mention your favorite candidate. 
# If the comment/submission has positive sentiment, then upvote it; 
# if the comment/submission has a negative sentiment, then downvote it.

import praw
import datetime
import time
import random
from textblob import TextBlob

reddit = praw.Reddit('bot')

submission_url = 'https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

while True:
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    submission.comments.replace_more(limit=None)
    all_comments=submission.comments.list()

    print('len(all_comments)=',len(all_comments))

    not_my_comments = []
    for comment in all_comments:
        #print('comment.author=',comment.author)
        #print('type(comment.author)=',type(comment.author))
        if str(comment.author) !='csci040-bot':
            not_my_comments.append(comment)

    print('len(not_my_comments)=',len(not_my_comments))

    numupvote = 0
    numdownvote = 0
    for comments in not_my_comments: 
        # for not_my_comments in range(0,1000):
        if 'biden' in comments.body.lower() or 'bernie' in comments.body.lower() or 'sanders' in comments.body.lower():
            testimonial = TextBlob(comments.body)
            testimonial.sentiment.polarity
            if testimonial.sentiment.polarity >= 0:
                comments.upvote()
                numupvote+=1
            elif testimonial.sentiment.polarity < 0:
                comments.downvote()
                numdownvote+=1
            else: 
                pass

    print('number of upvotes=', numupvote)
    print('number of downvote=', numdownvote)

    numsubupvote = 0
    numsubdownvote = 0
    for submission in reddit.subreddit('BotTown2').hot(limit=5):
        if 'bernie' in submission.title.lower() or 'biden' in submission.title.lower() or 'sanders' in submission.title.lower():
            testimonial = TextBlob(submission.title)
            testimonial.sentiment.polarity
            if testimonial.sentiment.polarity >= 0:
                submission.upvote()
                numsubupvote+=1
            elif testimonial.sentiment.polarity < 0:
                submission.downvote()
                numsubdownvote+=1
        else:
            pass
    
    print('number of subupvotes=', numsubupvote)
    print('number of subdownvote=', numsubdownvote)
    
    submission = random.choice(list(reddit.subreddit('BotTown2').hot(limit=None)))
    time.sleep(1)  