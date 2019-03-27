# ByeSubscribers
Saves Twitter list subscribers to a .csv file to import as a block list.

Some people have been commenting that trolls will put them on a list against their will then share the list with their friends.
Subscribers of the list then engage in coordinated harassment against the unwilling 'members' of the list.

Twitter has yet to deploy an automatic defense or mass-block utility to defend against this.

This small program can help you automatically block Twitter list subscribers.
You give it a list name and who made it and it outputs a .csv file of user id's that you can input as a block list.

I'm putting this on Github now because I don't know if I'll be able to host it on a separate website yet.

## Pre-reqs:
- Python
- A twitter dev account for 4 credentials that let you play with their api. This is fast (less then a day for me) and it is easy to [apply](https://developer.twitter.com/en/apply-for-access.html)
- The tweepy package, a Python wrapper for the Twitter API. You can download using pip or [conda](https://anaconda.org/conda-forge/tweepy). [[Docs]](http://docs.tweepy.org/en/3.7.0/)


## How to Use:
- Pull up twitter_credentials.py. Copy and paste the 4 values from your twitter dev account under "Keys and Tokens."
- Pull up byesub.py and change lines 24-26 to include the file you want to output to, the list creator, and the list slug.
  - Line 24: include the .csv file extension
  - Line 25: the @username
  - Line 26: the list slug is the bit in the URL after /lists/.
- In the command line, run python byesub.py
- Give twitter the .csv for a block list. Described [here.](https://help.twitter.com/en/using-twitter/advanced-twitter-block-options)
