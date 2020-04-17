from time import sleep
from random import choice

def fakeUserWait():
    #Set list of nums for random sleep time:
    sleep_nums = [num for num in range(10, 25)]
    #Return a random sleep time:
    return sleep(choice(sleep_nums))


if __name__ == "__main__":
    fakeUserWait()