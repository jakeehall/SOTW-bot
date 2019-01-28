# SOTW-bot [![Build Status](https://travis-ci.org/jakeehall/SOTW-bot.svg?branch=master)](https://travis-ci.org/jakeehall/SOTW-bot)
SOTW-bot is a Reddit bot for selecting a random song each week and then posting it on the given Subreddit.

SOTW-bot is used in the following Subreddits:
* [r/KidCudi](https://www.reddit.com/r/KidCudi/)
* More coming soon!

Feel free to add your subreddit to the list!

#### Notes:
##### Users:
* The SOTW bot account must be a moderator on the given Subreddit
* SOTW will always be the first sticky on the given Subreddit
##### Developers:
* If selected songs aren't added to the history table in the database, then selected songs may be duplicates of recently selected songs.

## Setting Up
Start by cloning or downloading a copy of all the files from this repo.
### Bot Info
[Settings_Template.py](./Settings_Template.py) is where the bots information is stored. Fill out the file with the correct information, save it, and rename it to Settings.py

You will need the following information:
```
client_id = ''      //Generated by Reddit, See Below!
client_secret = ''  //Generated by Reddit, See Below!
username = ''       //Bot username
password=''         //Bot password
subreddit=''        //Subreddit to post to
flairCSS=''         //For Old Reddit, name of css class, if used
database=''         //Any name that matches your SQLite DB file
```
##### Generating client_id and client_secret
1. Create and log into your SOTW account. (DO NOT USE YOUR PERSONAL REDDIT ACCOUNT)
2. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps), scroll to the bottom of the page and click the "create another app..." button.
3. Choose whatever name you like, select the "script" radio button, choose a fitting description, in the about URL put a link to this GitHub page, and for the Redirect URI put "http://localhost", and finally click the "create app" button.
4. You will now see a new new item with the name you chose under "developed applications". Click the "edit" link to see more information.
5. Look for the client_id and client_secret information as illustrated below.
![alt text](https://i.imgur.com/qsj6To5.png "Client I.D. and Client Secret Helper Image")

### Database
database.db is also provided, and is a template database that can be used, with the required tables and fields already created. To get the bot fully up and running open the database in [SQLite Browser](https://sqlitebrowser.org) and add all of the songs you wish to select from into the Song_Index table.
##### Note: all of the fields in Song_Index are required.
The History table can be left blank as it will automatically be generated as songs are selected.

### Crontab
Crontab comes with Linux and allows the scheduling of tasks for automation. This is what runs the SOTW-bot script every week, once a week.

In [schedule.cron](./schedule.cron) you will see the following format:
```
0 18 * * 5 cd /home/USER && /usr/bin/python /home/USER/SOTW-bot
```
This means the bot posts every week on Friday at 6pm.
##### IMPORTANT: The posting time is relative to the time zone set on the server where the script is running. For example, if your servers time is set to Eastern Time US (GMT-4) then the script will post at 6pm Eastern Time, but if the server time is set to Pacific Time US (GMT-7) then the script will post at 6pm Pacific Time US.
##### ALSO: Change "USER" to the username on your Linux server, you should NOT be executing this script as root.
You're welcome to change the cron job to whatever time you prefer, but I've found that this time works well for getting the most visibility in the US. There's plenty of resources and generators for crontab so I won't explain how to use it here. Just remember if you do modify the time, make sure you keep the tail of the command the same "cd /home/USER && /usr/bin/python /home/USER/SOTW-bot".

After Crontab is configured run the following command:
```
crontab schedule.cron
```
