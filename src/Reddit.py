import praw #Reddit Wrapper

class Reddit:
    def __init__(self, Settings, VERSION):
        self.rbot = Settings
        self.VERSION = VERSION
        # Auth Bot with Reddit
        reddit = praw.Reddit(client_id = self.rbot.client_id,
                             client_secret = self.rbot.client_secret,
                             user_agent = "SOTW-bot v"+self.VERSION,
                             username = self.rbot.username,
                             password = self.rbot.password)
        # Set the Subreddit
        self.subreddit = reddit.subreddit(self.rbot.subreddit)


    def post(self, SOTWNumber, song):
        # Print posting message
        print("Posting to r/"+self.rbot.subreddit+"...")

        # Create Post
        print("Creating Post")
        #post = subreddit.submit('\"'+title+'\"', url=imgURL)
        post = self.subreddit.submit('\"'+song.title+'\" - '+song.artist, selftext="")

        # Post Moderation
        post.mod.distinguish(how='yes')
        post.mod.approve()
        post.mod.sticky(state=True, bottom=False)
        post.mod.flair(text='SOTW #' + SOTWNumber, css_class=self.rbot.flairCSS)

        print("Creating Comment")
        # Comment a Stickied Post with Moderator Distinction
        description =   "||SOTW #"+SOTWNumber+"|\n" + \
                        "|:-|:-|\n" + \
                        "|Track|"+song.track+". "+song.title+"|\n" + \
                        "|Album|"+song.album+"|\n" + \
                        "|Artist|"+song.artist+"|\n" \
                        "|Year|"+song.year+"|\n\n" + \
                        "Quote:\n" + \
                        song.quote+"\n\n" + \
                        "Credits:\n" + \
                        song.credits+"\n\n" + \
                        "#[Get the iOS Shortcut](https://www.icloud.com/shortcuts/0781447519354cb393be1125e928eea0)\n\n" + \
                        "^([SOTW-bot v"+self.VERSION+"](https://github.com/jakeehall/SOTW-bot) by [JakeNation4](https://www.reddit.com/user/JakeNation4))"
        post.reply(description).mod.distinguish(how='yes', sticky=True)

        # Print on Completion
        print("Success!")
