#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyfcm import FCMNotification
import datetime
import random
import string
import time
import matplotlib.pyplot as plt
import numpy as np

def connect():
    push_service = FCMNotification(api_key=raw_input('Insert your Firebase Cloud Messaging Server key: '))
    registration_id = raw_input('Insert the instance ID Token of client: ')
    return push_service, registration_id


def send_50times_rand_payload(push, id):
    start = time.time()

    for i in range(50):
        message_title = "Message #%s" % (i + 1)
        curr_time = datetime.datetime.now()
        message_body = str(curr_time) + ": "
        rand_text = "".join([random.choice(string.letters) for j in range(random.randint(10, 300))])
        push.notify_single_device(registration_id=id, message_title=message_title,
                                  message_body=(message_body + rand_text))

    return time.time() - start


def get_inter_arrival_rate(push, id, payload=200):
    time_sum = 0
    text = "a" * payload
    for i in range(10):
        start = time.time()
        message_title = "Message #%s" % (i + 1)
        curr_time = str(datetime.datetime.now())
        message_body = curr_time + ": " + text
        push.notify_single_device(registration_id=id, message_title=message_title,
                                  message_body=message_body)
        time_sum += (time.time() - start)

    return time_sum / 10


def create_message(num_chars):
    message_body = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(num_chars))
    return message_body


def send_fixed_messages(push_service, registration_id, size_message=0, num_messages=25):
    message_title = "Message"
    message_body = create_message(size_message)
    curr_time = time.time()
    for i in range(num_messages):
        push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                          message_body=message_body)
    delta = (time.time() - curr_time)

    return delta


def send_messages_with_plot(push_service, registration_id, num_messages=50, size_message=200):
    message_title = "Message"
    message_body = create_message(size_message)
    curr_time = time.time()
    performance = []
    for i in range(num_messages):
        push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                          message_body=message_body)
        delta = (time.time() - curr_time)
        performance.append(delta)

    plt.clf()
    plt.plot(np.arange(0, len(performance)), performance)
    plt.xlabel("messages")
    plt.ylabel("time (seconds)")
    plt.title("Performance degrading")
    plt.savefig("performance.png")
    plt.show()


if __name__ == '__main__':
    push_service, registration_id = connect()
    # push_service = FCMNotification(api_key="AAAAU8Vo7C4:APA91bHpu-T-CArTfaTjMQ0CeCNlZ2c81afB2SeFtGyouutvUt7QURvbjhzQkZfdsul_ToIvWleH2ZhTtnAp_X4R0n9htiUqlvzZTHbks2boxtl6VRUOtu3ET0Q4X8mJpxv8xLEW4MUg")
    # registration_id = "d0B81WTvzqU:APA91bG97v-r4vHgzlSOPFI2Mid0rH3io4l-bLTAgYtQDjKeTyu4fkLdiatA7Bj-xz9qqT69CSe5zC6OZEcOtQnMwB8o_-XGZefO2fiffWKPomofq3ujWrkKENj2xAZbwAnEqe7E7d4G"

    # exercise 1
    # print("Average time to send 50 random messages: %s seconds." % send_50times_rand_payload(push_service, registration_id))

    # exercise 2
    # time_list = []
    #
    # mess_size = 2
    #
    # for i in range(0, 10):
    #     print("------ITERATION NUMBER {} -------- ".format(str(i+1)))
    #     delta = send_fixed_messages(push_service, registration_id, mess_size, 25)
    #     time_list.append(delta)
    #
    # print("Average time for 25 messages of size {}:".format(mess_size), (sum(time_list) / float(len(time_list))))

    # exercise 3
    # print("Inter arrival date of average message payload: %s seconds." % get_inter_arrival_rate(push_service, registration_id))

    # exercise 4
    send_messages_with_plot(push_service, registration_id, num_messages=200)
