import random
import time
import webbrowser

 
while True:
    sites = random.choice(["twitter.com","tiktok.com","wim.no","instagram.com","facebook.com"])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randint(2,5) 
    time.sleep(seconds)
