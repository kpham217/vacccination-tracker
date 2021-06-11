import tweet_bot_credential
# import schedule
import time
import tweepy
import sched
import threading

WAIT_SECONDS = 900
counter = -0
import itertools



def set_global():
    global counter
    counter += 1
    if counter == 3:
        counter = 0


def initialize_api():
    api = tweet_bot_credential.create_api()
    return api


def create_tweet(api, site_list):
    set_global()
    new_list = site_list[counter]
    alist = [0, 1, 2, 3, 4]

    combinations_object = itertools.combinations(alist, 2)
    combinations_list = list(combinations_object)
    # combinations_list = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    content = f"💉 Earliest vaccination dates\n\n"
    for item in combinations_list:
        if len(new_list[item[0]]['siteName'] + new_list[item[1]]['siteName']) <100:
            new = f"📍 {new_list[item[0]]['siteName']}\n🗓 {new_list[item[0]]['readableBookingTime']}\n\n"
            new += f"📍 {new_list[item[1]]['siteName']}\n🗓 {new_list[item[1]]['readableBookingTime']}\n\n"
            content = content + new
            break
    content += "Book here: https://novascotia.flow.canimmunize.ca/en/9874123-19-7418965?fbclid=IwAR0mx8GuTcL47-cqAEafer6xSHSAOZaedJcPx_n5XcDrSqWGn4MoxmMnC0c\n"
    content += "#NS #COVID19\n"
    print(content)

    # for item in new_list:
    #     new = f"📍 {item['siteName']}\n🗓 {item['readableBookingTime']}\n\n"
    #     content = content + new
    # content += "Book here: https://novascotia.flow.canimmunize.ca/en/9874123-19-7418965?fbclid=IwAR0mx8GuTcL47-cqAEafer6xSHSAOZaedJcPx_n5XcDrSqWGn4MoxmMnC0c\n"
    # content += "#NS #COVID19\n"
    # print(content)
    try:
        # api.update_status(content)
        print('> Content successfully posted on Twitter!')
    except tweepy.TweepError:
        print('Tweep Error:Status is a duplicate.')

    threading.Timer(WAIT_SECONDS, create_tweet, args=(api, site_list)).start()


def create_bot(array, region_count):
    # WAIT_SECONDS = 120
    time.sleep(60)
    # scheduler = sched.scheduler(time.time, time.sleep)
    # scheduler = threading.Timer
    # initiate()
    api = initialize_api()

    # schedule.every(2).minutes.do(create_tweet, api=api, site_list=array)
    # periodic(scheduler, 120, create_tweet, actionargs=(api, array))
    # periodic(scheduler, 60, create_tweet, actionargs=
    create_tweet(api, array)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
