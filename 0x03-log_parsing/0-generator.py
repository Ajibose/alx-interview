#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

"""for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()"""

sys.stdout.write('78.99.227.220 - [2017-02-05 23:25:51.534767] "GET /projects/260 HTTP/1.1" 401 724')
sys.stdout.flush()
