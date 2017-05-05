from pprint import pprint
import datetime
import time

pprint("current timestamp(datetime): " + str(datetime.datetime.now()))
pprint("current timestamp: " + str(time.time()))
pprint("1. current timestamp(integer): " + str(int(time.time())))

print("working 1")
print("working 2")
print("working 3")

pprint("2. current timestamp(integer): " + str(int(time.time())))