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
sys.stdout.write('68.249.9.20 - [2017-02-05 23:31:22.452556] "GET /projects/260 HTTP/1.1" 200 711\n')
sys.stdout.flush()
sys.stdout.write('99.196.100.39 - [2017-02-05 23:31:22.954433] "GET /projects/260 HTTP/1.1" 401 658\n')
sys.stdout.flush()
sys.stdout.write('128.230.61.246 - [2017-02-05 23:31:23.258076] "GET /projects/260 HTTP/1.1" Hello 292\n')
sys.stdout.flush() 
sys.stdout.write('116.82.223.35 - [2017-02-05 23:31:24.112360] "GET /projects/260 HTTP/1.1" 301 842\n')
sys.stdout.flush() 
sys.stdout.write('Holberton - [2017-02-05 23:31:25.003550] "GET /projects/260 HTTP/1.1" 400 12\n')
sys.stdout.flush()
sys.stdout.write('7.179.133.121 - [2017-02-05 23:31:25.003550] "GET /projects/260 HTTP/1.1" 400 12\n')
sys.stdout.flush()
sys.stdout.write('188.213.11.218-[2017-02-05 23:31:21.690755] "GET /projects/260 HTTP/1.1" 401 1000\n')
sys.stdout.flush() 
sys.stdout.write('128.230.61.246 - [2017-02-05 23:31:23.258076] "GET /projects/260 HTTP/1.1" 301 292\n')
