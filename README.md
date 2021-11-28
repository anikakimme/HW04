# HW 04: Reddit Bot

## Politician
My bot is supporting **Bernie Sanders**.

## Favorite Thread
Here is a [link](https://old.reddit.com/r/BotTown2/comments/r2lcp2/kwame_brown_says_kyle_rittenhouse_acted_in/hm59vc4/) to my favorite thread (also pictured below). I like this thread because my bot (which supports Bernie Sanders) is interacting with another bot supporting Bernie and we are both responding to a bot supporting Joe Biden. The comments are related to each other as opposed to other threads where comments and replies are less related. 
![Screen shot](/Users/anikakimme/Desktop/Bernie.jpg)

## Output
```
Anikas-MacBook-Air:BOT anikakimme$ python3 bot_counter.py --username=csci040-bot
len(comments)= 854
len(top_level_comments)= 65
len(replies)= 789
len(valid_top_level_comments)= 51
len(not_self_replies)= 789
len(valid_replies)= 551
========================================
valid_comments= 602
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
## Score
My score should be a **34** for the following reasons:
1. Completing each task in the `bot.py` file (18 points)
1. Creating this github repository (2 points)
1. **Extra credit 1:** making 100 valid comments (2 points)
    1. See output above
1. **Extra credit 2:** making 500 valid comments (2 points)
    1. See output above
1. **Extra credit 4:** making my bot create new submissions instead of new comments (2 points)
    1. See `extracredit4.py`
    1. This file shows that I created both self posts and link posts
1. **Extra credit 5:** Creating 5 bots that all made 500 valid comments (2 points)
    1. See `bot2.py`,`bot3.py`,`bot4.py`,`bot5.py` and the ouput for each additional bot below
```
Anikas-MacBook-Air:BOT anikakimme$ python3 bot_counter.py --username=secondcs40bot
len(comments)= 798
len(top_level_comments)= 56
len(replies)= 742
len(valid_top_level_comments)= 52
len(not_self_replies)= 742
len(valid_replies)= 523
========================================
valid_comments= 575
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
```
Anikas-MacBook-Air:BOT anikakimme$ python3 bot_counter.py --username=thirdcs40bot
len(comments)= 855
len(top_level_comments)= 68
len(replies)= 787
len(valid_top_level_comments)= 58
len(not_self_replies)= 787
len(valid_replies)= 557
========================================
valid_comments= 615
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
```
Anikas-MacBook-Air:BOT anikakimme$ python3 bot_counter.py --username=fourthcsbot
len(comments)= 774
len(top_level_comments)= 62
len(replies)= 712
len(valid_top_level_comments)= 54
len(not_self_replies)= 712
len(valid_replies)= 478
========================================
valid_comments= 532
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
```
Anikas-MacBook-Air:BOT anikakimme$ python3 bot_counter.py --username=fifthcsbot
len(comments)= 932
len(top_level_comments)= 61
len(replies)= 871
len(valid_top_level_comments)= 51
len(not_self_replies)= 871
len(valid_replies)= 614
========================================
valid_comments= 665
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
1. **Extra credit 6:** Having my bot reply to the most highly upvoted comments (2 points)
    1. See `bot.py` file
1. **Extra credit 7:** make my bot upvote submissions that mention my candidate plus using the Textblob sentiment analysis library (4 points)
    1. See `extracredit7.py` file