




from ast import While
from imghdr import what
from shutil import which
import time

z = 0
while z <= 5:
    x = 0
    n = 0
    while x <= 5:
        try:
            uss = open('ussers.txt', 'r')
            ff = uss.readlines()
            z = len(ff)
            print(ff[n][:-1])
            n = n + 1
            time.sleep(5)
        except:break
    z = z + 1