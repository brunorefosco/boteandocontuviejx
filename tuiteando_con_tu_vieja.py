import tweepy
from secret import *
import random
import time


def login():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api


def tuitear_repetido_random():
    #tuitea linea al azar del archivo
    file = open("gerundios.txt", "r", encoding='utf-8')
    text = file.readlines() 
    file.close()
    while True:
        rand = random.randrange(len(text))
        verbo = text[rand].replace('\n', '')
        print("Intentando tuitear {} con tu vieja".format(verbo))
        tuit = "{} con tu vieja".format(verbo)

        try:
            api.update_status(status=tuit)
            print("tuiteado {}".format(text[rand]))
        except Exception as e:
            print(e.reason)
        time.sleep(300)


if __name__ == "__main__":
    api = login()
    tuitear_repetido_random()