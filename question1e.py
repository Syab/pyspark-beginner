import math
import os
import random
import re
import sys

the_dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}

print(the_dic['k1'][3]['tricky'][3]['target'][3])
