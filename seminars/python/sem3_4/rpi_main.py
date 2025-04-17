import random
import sys
import select

while True:
    if select.select([sys.stdin],[],[],0)[0]:
        received = sys.stdin.readline().strip()
        if received == "T?":
            print(random.random() * 100)
