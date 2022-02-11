import random
import praw

r = praw.Reddit(
    client_id="################",
    client_secret="#################",
    password="##########",
    user_agent="Harry Potter Bot",
    username="###########"
)

hp_quotes= [
'“It does not do to dwell on dreams and forget to live.” — Albus Dumbledore',
'""There are all kinds of courage," said Dumbledore, smiling. "It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends."',
'""The truth." Dumbledore sighed. "It is a beautiful and terrible thing, and should therefore be treated with great caution."',
'“Fear of a name increases fear of the thing itself.” — Albus Dumbledore',
'“There are some things you can’t share without ending up liking each other, and knocking out a twelve-foot mountain troll is one of them.”',
'“"Ah, music," he said, wiping his eyes. "A magic beyond all we do here!” — Albus Dumbledore',
'“I hope you’re pleased with yourselves. We could all have been killed – or worse, expelled. Now if you don’t mind, I’m going to bed.” — Hermione Granger',
'“Your mother died to save you. If there is one thing Voldemort cannot understand, it is love. Love as powerful as your mother’s for you leaves it’s own mark. To have been loved so deeply, even though the person who loved us is gone, will give us some protection forever.” — Albus Dumbledore',
'“As much money and life as you could want! The two things most human beings would choose above all – the trouble is, humans do have a knack of choosing precisely those things that are worst for them.” — Albus Dumbledore',
'"Yer a wizard, Harry!" — Rubeus Hagrid',
'""Don’t play," said Hermione at once. "Say you’re ill," said Ron. "Pretend to break your leg," Hermione suggested. "Really break your leg," said Ron.',
'""I know some things," he said. "I can, you know, do math and stuff.” — Harry Potter',
'“Harry then did something that was both very brave and very stupid.”',
'“The wand chooses the wizard.” — Garrick Ollivander',
'“Funny way to get to a wizards’ school, the train. Magic carpets all got punctures, have they?” — Uncle Vernon',
'“Troll — in the dungeons — thought you ought to know.” — Professor Quirrell',
'“Training for the ballet, Potter?” — Draco Malfoy',
'“Of all the trees we could’ve hit, we had to get one that hits back.” — Ron Weasley',
'“When in doubt, go to the library.” — Ron Weasley',
'“Hearing voices no one else can hear isn’t a good sign, even in the wizarding world.” — Ron Weasley',
'“You will also find that help will always be given at Hogwarts to those who ask for it.” — Albus Dumbledore',
'""Do I look stupid?" snarled Uncle Vernon, a bit of fried egg dangling from his bushy mustache.”',
'“Honestly, if you were any slower, you’d be going backward.” — Draco Malfoy',
'“Snape was looking as though the first person to ask him for a Love Potion would be force-fed poison.”',
'""Jiggery pokery!" said Harry in a fierce voice. "Hocus pocus — squiggly wiggly —" "MUUUUUUM!" howled Dudley, "He’s doing you know what!""',
'“Fawkes is a phoenix, Harry. Phoenixes burst into flame when it is time for them to die and are reborn from the ashes.” — Albus Dumbledore',
'""Offend Dobby!" choked the elf. "Dobby has never been asked to sit down by a wizard — like an equal.""',
'“I’ll be in my bedroom, making no noise and pretending I’m not there.” — Harry Potter',
'“It is our choices, Harry, that show what we truly are, far more than our abilities.” — Albus Dumbledore',
'“Fame is a fickle friend, Harry. Celebrity is as celebrity does. Remember that.” — Gilderoy Lockhart'
]

def bot_comment():
    for comment in r.subreddit("MyHarryPotterBot").stream.comments(skip_existing=True):
        rand_index = random.randint(0, len(hp_quotes)-1)
        rand_quote = hp_quotes[rand_index]
        if ("Harry Potter" in comment.body or "harry potter" in comment.body or "HARRY POTTER" in comment.body):
            comment.reply(rand_quote)

def retry_forever():
    while True:
        try:
            bot_comment()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    run_forever()





