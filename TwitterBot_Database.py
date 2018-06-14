import sqlite3, random, sys

class quoteDatabase():

    def __init__(self):
        #creates a connection to freebsd database
        self.conn = sqlite3.connect("freebsd_fortunes_clean.sl3")
        self.cur = self.conn.cursor()

    def getQuote(self):
        #Randomly selects a line
        #checks if the line is under 140 characters (Twitter Limit)
        #if over, gets another line and repeats
        self.randLine = random.randrange(1,1000)
        self.cur.execute("SELECT * FROM fortunes")

        self.row = self.cur.fetchall()
        for rows in self.row:
            if int(rows[0]) == int(self.randLine):
                if int(rows[2]) <= 140:
                    return str('"' + rows[3] + '"')
                else:
                    self.randLine = random.randrange(self.randLine, 1000)

class mySettings():
#assume that we already have a table
#connect contents of table to program
    
    def __init__(self):
        #creates a connection to settings database
        self.conn = sqlite3.connect("BotSettings.db")
        self.cur = self.conn.cursor()
        self.startup()
        
    def startup(self):
        #gets information from database - settings.db
        #settings is set as | ID/ROW | Frequency | StartDate | StartTime|
        #the settings represent columns
        self.cur.execute("SELECT * FROM Settings")
        self.rows = self.cur.fetchone()
        self.delay = self.rows[1]
        self.frequency = self.rows[2]

    def updateDelay(self,newDelay):
        #super - dropdown menu
        #super - select
        self.delay = newDelay
        self.cur.execute("""
                         UPDATE Settings
                         SET delay = ?
                         WHERE id = 1
                         """,(self.delay,))
        self.conn.commit()


    def updateFrequency(self,newFreq):
        #super - dropdown menu
        #super - select
        self.frequency = newFreq
        self.cur.execute("""
                        UPDATE Settings
                        SET frequency = ?
                        WHERE id = 1
                        """,(self.frequency,))
        self.conn.commit()
