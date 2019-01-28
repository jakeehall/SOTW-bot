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
class RedditBotTest:
    client_id = ''
    client_secret = ''
    username = ''
    password=''
    subreddit=''
    flairCSS=''
    database='database.db'
    historyEnabled = False # SOTW history will not be saved to database
    postingEnabled = False # SOTW will not be posted to Reddit

class TravisCI:
    database= 'database_template.db'
    historyEnabled = True # SOTW history will not be saved to database
    postingEnabled = False # SOTW will not be posted to Reddit
