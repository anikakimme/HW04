import praw
import random
import datetime
import time

# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "Bernie Sanders is the [BEST] polictician [EVER]. He is so [NICE]. I [THINK] everyone should [VOTE FOR] him.",
    "I don't [UNDERSTAND] why [BERNIE] lost the [ELECTION]. He was the [BEST] candidate for the [COUNTRY]. ",
    "If you don't [LIKE] [BERNIE] try watching a [MOVIE] about him. You might find one on [NETFLIX] or [HULU].",
    "Bernie Sanders is a [GOOD] [POLITICIAN]. He can [SPEAK] well and he is good at [HELPING] others. This is why you should [CONSIDER] supporting him.",
    "Bernie has a pet [DOG]. [HIS] name is [FRED]. A vote for Bernie is a vote for [FRED]. [THEREFORE] [YOU] should vote for Bernie.",
    "[BERNIE] [WRITES] good policies about [HEALTHCARE]. He has [A LOT OF] policies. He has [VERY] different polices than [TRUMP]. ",
    "Bernie is [FRIENDS] with [TAYLOR SWIFT]. They [BAKE] [COOKIES] and [EAT] it together. A vote for Bernie is a vote for [TAYLOR SWIFT].",
]

replacements = {
    'BEST': ['best', 'greatest', 'finest', 'most wonderful' ],
    'EVER': ['ever','in the world', 'in the country', 'in all of time'],
    'NICE': ['nice','kind','caring','creative','cool','smart',],
    'THINK': ['think','believe','am confident','assume'],
    'VOTE FOR': ['vote for', 'support', 'submit a ballot for'],
    'UNDERSTAND': ['understand','know', 'comprehend'],
    'BERNIE': ['Bernie','Bernie Sanders','Senator Sanders', 'Senator Bernie Sanders'],
    'ELECTION': ['election','primaries', 'democratic primaries'],
    'COUNTRY': ['country','United States', 'US', 'Vermont'],
    'LIKE': ['love', 'like','adore'],
    'MOVIE': ['movie', 'film', 'tv show', 'documentary','youtube video'],
    'NETFLIX': ['hulu','netflix','Apple TV','Amazon','Peacock', 'HBO Max'],
    'HULU': ['hulu','netflix','Apple TV','Amazon','Peacock', 'HBO Max'],
    'GOOD': ['good', 'great', 'excellent', 'amazing','pretty good'],
    'POLITICIAN': ['politician', 'senator', 'candidate', 'person'],
    'SPEAK': ['speak','talk','give speeches', 'communicate'],
    'HELPING': ['helping','assisting', 'aiding'],
    'CONSIDER': ['consider','thing about','contemplate','ponder'],
    'DOG': ['dog','cat','hamster','guinea pig','turtle','fish','horse','cow','sheep','goat','hippo','wolf','elephant'],
    'HIS': ['his','her', 'their'],
    'FRED': ['Fred','George','Ron','Harry','Hermione','Ginny','Severus Snape','Molly','Bill','Arthur','Luna'],
    'THEREFORE': ['Therefore','As a result', 'Consequently','As a consequence'],
    'YOU': ['you','we','we all','you guys','everyone','the country'],
    'WRITES': ['writes','composes', 'creates','drafts','compiles','formulates','produces'],
    'HEALTHCARE': ['healthcare', 'the environment','education','childcare','the economy','minimum wage'],
    'A LOT OF': ['a lot of', 'a good number of', 'many'],
    'VERY': ['very', 'extremely','extrodinarily','exceedingly','exceptionally','vastly','hugely'],
    'TRUMP': ['Trump','Donald Trump','George Bush','Ronald Reagan','Richard Nixon', 'Mike Pence'],
    'FRIENDS': ['friends','pals','companions','acquintances','soul mates'],
    'TAYLOR SWIFT': ['Taylor Swift', 'Adele','Selena Gomez','Ariana Grande','Justin Bieber'],
    'BAKE': ['bake', 'cook','make'],
    'COOKIES': ['cookies','cake','tiramisu','tarts','pie'],
    'EAT': ['eat','consume','devour']
    }


def generate_comment():

    s=random.choice(madlibs)
    for k in replacements.keys():
        s=s.replace('['+k+']', random.choice(replacements[k]))
    return s

# connect to reddit 
reddit = praw.Reddit('bot4')

# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://old.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True: ###### change to while True later

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    
    submission.comments.replace_more(limit=None)
    all_comments=submission.comments.list()
   
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        #print('comment.author=',comment.author)
        #print('type(comment.author)=',type(comment.author))
        if str(comment.author) !='fourthcsbot':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not

        comments_without_replies = []
        for comments in not_my_comments:
            replied_to_comment = False
            for replies in comments.replies:
                if str(replies.author) =='fourthcsbot':
                    replied_to_comment=True 
            if replied_to_comment == False:
                comments_without_replies.append(comments)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message


        try: 
            # comment = random.choice(comments_without_replies)
            comment = sorted(comments_without_replies, key=lambda x: x.score, reverse=True)[0]   #upvote extra credit 
            text= generate_comment()
            comment.reply(text)
        except praw.exceptions.APIException:
            print('not replying to a deleted comment')
        except IndexError:
            print('not replying because replied to all comments that are not mine')
        

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    submission = random.choice(list(reddit.subreddit('BotTown2').hot(limit=5)))

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(5)
