import math
import os
import random
import re
import sys

substr = 'elephant'


def count_ele(str):
    num_occur = 0
    if substr in str:
        num_occur = str.count(substr)

    return num_occur


_str = input()
tolowstr = _str.lower()

print (count_ele(tolowstr))