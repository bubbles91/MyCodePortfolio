import random
import praw

r = praw.Reddit(
    client_id="################",
    client_secret="#################",
    password="##########",
    user_agent="Harry Potter Bot",
    username="###########"
)

print(r.user.me())

hp_quotes= [
    'Yer a wizard Harry.',
    'There are some things you can’t share without ending up liking each other, and knocking out a twelve-foot mountain troll is one of them.',
    'I’ll be in my bedroom, making no noise and pretending I’m not there.',
    'I solemnly swear I am up to no good.',
    'Don’t let the muggles get you down.',
    'He can run faster than Severus Snape confronted with shampoo.'
]

for comment in r.subreddit("thisismybot").stream.comments():
    rand_index = random.randint(0, len(hp_quotes)-1)
    rand_quote = hp_quotes[rand_index]
    if ("Harry Potter" in comment.body):
        comment.reply(rand_quote)





