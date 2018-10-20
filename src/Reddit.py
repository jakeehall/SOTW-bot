from Settings import RedditBot as rbot #Reddit Bot Settings
import praw #Reddit Wrapper

class Reddit:
    def __init__(self, VERSION):
        self.VERSION = VERSION
        # Auth Bot with Reddit
        reddit = praw.Reddit(client_id = rbot.client_id,
                             client_secret = rbot.client_secret,
                             user_agent = "SOTW-bot v"+self.VERSION,
                             username = rbot.username,
                             password = rbot.password)
        # Set the Subreddit
        self.subreddit = reddit.subreddit(rbot.subreddit)


    def post(self, SOTWNumber, song):
        # Print posting message
        print("Posting to r/"+rbot.subreddit+"...")

        # Create Post
        #imgURL = "https://i.redd.it/hpeqoarknq7y.jpg"
        #post = subreddit.submit('\"'+title+'\"', url=imgURL)
        post = self.subreddit.submit('\"'+song.title+'\" - '+song.artist, selftext="")

        # Post Moderation
        post.mod.distinguish(how='yes')
        post.mod.approve()
        post.mod.sticky(state=True, bottom=False)
        post.mod.flair(text='SOTW #' + SOTWNumber, css_class=rbot.flairCSS)

        # Comment a Stickied Post with Moderator Distinction
        description =   "*"+song.track+". "+song.title+"*\n\n" + \
                        "*"+song.album+"*\n\n" + \
                        "*"+song.artist+"*\n\n" + \
                        "*"+song.year+"*\n\n" + \
                        "Quote:\n" + \
                        song.quote+"\n\n" + \
                        "Credits:\n" + \
                        song.credits+"\n\n" + \
                        "##### SOTW-bot v"+self.VERSION+" by u/JakeNation4"
        post.reply(description).mod.distinguish(how='yes', sticky=True)

        # Print on Completion
        print("Success!")
