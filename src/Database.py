import os
import sqlite3 #Database
from sqlite3 import Error
import datetime #Date
from Song import Song

class Database:
    def __init__(self, databaseFile):
        # Connect to the Database
        self.databaseFile = databaseFile
        try:
            self.conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), '..', self.databaseFile))
            self.conn.text_factory = str #For Python 2 to convert utf8 to str
            print("Connected to: "+self.databaseFile)
        except Error as e:
            print(e)


    def randomSong(self, limit=1):
        # Select new Song randomly without repeats
        cursor = self.conn.execute("""
            SELECT * FROM Song_Index SI
                LEFT JOIN (
                    SELECT * FROM History
                    ORDER BY SOTW DESC
                    LIMIT (SELECT COUNT(*)-1 FROM Song_Index)) H
                ON SI.id = H.id
            WHERE H.id IS NULL
            ORDER BY RANDOM()
            LIMIT ?;""",
            (limit,)
        )
        col = cursor.fetchone()
        song = Song(col)
        print("Selected: ")
        print(song.title, song.album, song.artist, song.year)
        return song


    def selectSong(self, title):
        # Select new Song from a give title
        cursor = self.conn.execute("""
            SELECT * FROM Song_Index
            WHERE Title = ?;""",
            (title,)
        )
        col = cursor.fetchone()
        song = Song(col)
        print("Selected: ")
        print(song.title, song.album, song.artist, song.year)
        return song


    def addSongToHistory(self, song):
        # Add Selected SOTW to History
        self.conn.execute("""
            INSERT INTO History (Title, id, Date)
            VALUES (?, ?, ?);""",
            (song.title, song.songID, datetime.datetime.now())
        )
        # Incriment the times this song has won SOTW
        self.conn.execute("""
            UPDATE Song_Index
            SET Times_Won = Times_Won + 1
            WHERE id = ?;""",
            (str(song.songID),)
        )
        self.conn.commit()
        print("Added to History")


    def getSongOfTheWeekNumber(self):
        # Get SOTW number from max SOTW enrty in History
        cursor = self.conn.execute("SELECT MAX(SOTW) FROM History;")
        return str(cursor.fetchone()[0])


    def __del__(self):
        self.conn.close()
        print("Disconnected from: "+self.databaseFile)
