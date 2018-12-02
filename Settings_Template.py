# SOTW-bot account must be a moderator of the given subreddit
class RedditBot:
    client_id = ''
    client_secret = ''
    username = ''
    password=''
    subreddit=''
    flairCSS=''
    database='database.db'


# FOR DEVELOPERS ONLY!
# CHANGE "RedditBot" TO "RedditBotTest" IN __main__.py
class RedditBotTest:
    historyEnabled = False # SOTW history will not be saved to database
    postingEnabled = False # SOTW will not be posted to Reddit
    client_id = ''
    client_secret = ''
    username = ''
    password=''
    subreddit=''
    flairCSS=''
    database='database.db'
