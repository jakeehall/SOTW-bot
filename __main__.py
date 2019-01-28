if __name__ == "__main__":
    import sys
    import importlib
    from src.Reddit import Reddit
    from src.Database import Database
    VERSION = "1.4.0" # Version of SOTW-bot (DO NOT CHANGE)


    # Set rbot default settings
    className = "RedditBot"
    fileName = "Settings"
    # Set rbot settings based on CLI argument
    if(len(sys.argv) > 1):
        className = sys.argv[1] # Capture 2nd argument as Class to use for rbot
        if(len(sys.argv) > 2):
            fileName = sys.argv[2] # Capture 3rd argument as file name for rbot
    rbot = getattr(importlib.import_module(fileName), className) # import rbot


    # Select song, add it to history, and get its SOTW number
    db = Database(rbot.database) # Instantiate and connect to the database
    song = db.randomSong() # Randomly select new song
    SOTWNumber = str(db.getSongOfTheWeekNumber() + 1) # Incriment SOTW number
    if not hasattr(rbot, "historyEnabled") or rbot.historyEnabled:
        db.addSongToHistory(song) # Add song to History and incriment times won
    del db # Close the database


    # Reddit
    if not hasattr(rbot, "postingEnabled") or rbot.postingEnabled:
        reddit = Reddit(rbot, VERSION) # Instantiate and setup praw
        reddit.post(SOTWNumber, song) # Post SOTW to Reddit
