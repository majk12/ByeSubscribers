import tweepy # for python
import json # for parsing

import twitter_credentials # My own file of twitter creds for their API

# The main function that writes the username to a .csv file
def try_to_write(file_name, user_id):
    try:
        with open(file_name,'a') as tf:
            tf.write(user_id)
            tf.write("\n")
    except BaseException as e:
        print("Error writing to file %s" % str(e))
    return True

if __name__ == "__main__":
    # authenticate
    auth =  tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    # needs 3 Variables
    file_name = "my_file.csv"
    owner = ''
    slug = ''

    # returns list of User object
    # list <= 5000 people
    sub_list = api.list_subscribers(owner, slug, count = 5000)
    print("length of sub list: ", len(sub_list)) # sometimes doesn't match, idk why

    for s in sub_list:
        user_id = json.dumps(s._json['id'])
        try_to_write(file_name, user_id)
        ## Uncomment below to see associated screen names
        #screen_name = json.dumps(s._json['screen_name'])
        #print(screen_name)
