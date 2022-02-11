import math
import os
import random
import re
import sys

def get_speed_range(speedval):
    speedrange=''
    if (speedval <= 60):
        speedrange='Low speed'
    elif (speedval >= 61 and speedval <= 80):
        speedrange = 'Low speed'
    elif (speedval >= 61):
        speedrange='Fast Speed'
    return speedrange

print ("Enter speed value:")
_speed=int(input())
print(get_speed_range(_speed))
