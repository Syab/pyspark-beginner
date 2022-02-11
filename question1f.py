import math
import os
import random
import re
import sys

substr='elephant'
def check_ele(str):
    if substr in str:
        return True
    else:
        return False

_str=input()
str=_str.lower()
print (check_ele(str))