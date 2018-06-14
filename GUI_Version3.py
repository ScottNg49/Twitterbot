#TwitterBot Version 3
#MIT LICENSE
import TwitterBot_API as f
import TwitterBot_Database as n
from tkinter import *

access_token = '859601950332956672-bozSVH3zup1IwcTBjatx4kmTwPmgLBR'
access_secret = 'aSh0w8WHVGYhGSzVlVqNjcO99BWeS9dggoj6Spj4A93MS'
consumer_token = 'dcvMZLgtkadoPTY7RyCqZ6sim'
consumer_secret = 'kXm4AiXaEQ46NG4pn8CgIBMTuApwBFHsBhFCaV1hRMKlAQaKqv'

class GUI:
    def __init__(self, master):
        #calling functions from other .py files
        self.master = master
        master.title("TwitterBot")

        self.d = n.quoteDatabase()
        self.s = n.mySettings()
        self.t = f.TwitterNews(access_token,access_secret,
                               consumer_token,consumer_secret)
        self.message = self.d.getQuote()
        self.startGUI()

        self.timer = 10

    def startGUI(self):
        #creating labels, buttons, and frames
        #Labels  - string/text that cannot be interacted with user
        #Buttons - allows user interaction
        #Frame   - creates a frame to put labels inside 
        self.welcome = Label(self.master, text="Welcome to the Twitter Bot!")
        self.seperator1 = Frame(height=2, bd=1, relief=SUNKEN)

        self.tweet_frame = LabelFrame(self.master, text="Message to be Tweeted",
                                      bg="white",height=250,width=550)
        self.tweet_message = Label(self.master, text=self.message, bg="white")
        
        self.tweet_button = Button(self.master,
                                   text="Tweet Now",
                                   command=self.tweet)
        self.close_button = Button(self.master,
                                   text="Close",
                                   command=self.master.quit)
        self.nextT_button = Button(self.master,
                                   text="Next" ,
                                   command=self.next_quote)
        self.sched_button = Button(self.master,
                                   text="Schedule Tweet",
                                   command=self.schedule_tweet)

        #Grid is used to set and place the Labels, Buttons, and Frames
        #Top left of the window is row=0, column=0 (default=0)
        #Columnspan is the size of columns (default=1)
        #Rowspan is the size of rows (default=1)
        #Sticky is used for placement/justifcation
        #W = West or left justification based on row/column size
        #E = East or right justifcation based on row/column size
        #W+E = Centered justification based on row/column size


        self.welcome.grid(row=0, column=0, columnspan=5, sticky=W)
        self.seperator1.grid(row=1, column=0, columnspan=5,
                             sticky=W+E, padx=5, pady=5)
        
        self.tweet_frame.grid(row=2, column=0,
                              columnspan=5, rowspan=1,
                              sticky=W+E)
        self.tweet_message.grid(row=2, column=0,
                                columnspan=5, rowspan=1,
                                sticky=W+E)
        
        self.tweet_button.grid(row=4, column=0, columnspan=1, sticky=W+E)
        self.close_button.grid(row=4, column=1, columnspan=1, sticky=W+E)
        self.nextT_button.grid(row=4, column=2, columnspan=1, sticky=W+E)
        self.sched_button.grid(row=4, column=3, columnspan=1, sticky=W+E)

    def next_quote(self):
        #calls getQuote function from database file
        #cycles the label tweet_message
        #updates the tweet onto the GUI
        self.message = self.d.getQuote()
        self.tweet_message = Label(self.master, text=self.message,
                                   bg="white", height=7, width=4)
        self.tweet_message.grid(row=2, column=0, columnspan=5,
                                rowspan=1, sticky=W+E)

    def tweet(self):
        #calls tweetNow function
        try:
            self.t.tweetNow(self.message)
            self.tweet_label = Label(self.master,
                                     text="Message was tweeted at " +
                                     str(f.datetime.datetime.now().time()))
            self.tweet_label.grid(row=5, column=0, columnspan=2, sticky=W+E)
        except:
            self.tweet_label = Label(self.master,
                                     text="Message has already been tweeted! \
Press Next!")
            self.tweet_label.grid(row=5, column=0, columnspan=2, sticky=W+E)

    def schedule_tweet(self):
        #sets a messaged to be tweeted at a later time
        #user delay implementation needs to be added
        self.t.scheduleTweet(self.timer,self.message)
        self.tweet_label = Label(self.master,
                                 text="Delayed Message will be tweeted in " +
                                 str(self.timer) + " seconds")
        self.tweet_label.grid(row=5, column=0, columnspan=2, sticky=W+E)

    def delay_set(self):
        #set the delay for scheduled tweets
        #not implemented
        pass
        
if "__main__" == __name__:
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()
