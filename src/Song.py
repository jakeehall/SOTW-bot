class Song:
    def __init__(self, col):
        self.songID = col[0]
        self.title = str(col[1])
        self.album = str(col[2])
        self.artist = str(col[3])
        self.year = str(col[4])
        self.credits = str(col[5])
        self.quote = str(col[6])
        self.track = str(col[7])
        self.link = str(col[8])
