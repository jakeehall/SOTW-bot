if __name__ == "__main__":
    from Settings import RedditBot as rbot #Reddit Bot Settings
    from src.Reddit import Reddit
    from src.Database import Database


    VERSION = "1.2.0" #Version of SOTW-bot (DO NOT CHANGE)
    # Select song, add it to history, and get its SOTW number
    db = Database(rbot.database) # Instantiate and connect to the database
    song = db.randomSong() # Randomly select new song
    SOTWNumber = str(db.getSongOfTheWeekNumber() + 1) # Get the latest SOTW number
    if not hasattr(rbot, "historyEnabled") or rbot.historyEnabled:
        db.addSongToHistory(song) # Add song to History and incriment times won
    del db # Close the database


    # Reddit
    if not hasattr(rbot, "postingEnabled") or rbot.postingEnabled:
        reddit = Reddit(rbot, VERSION) # Instantiate and setup praw
        reddit.post(SOTWNumber, song) # Post SOTW to Reddit
