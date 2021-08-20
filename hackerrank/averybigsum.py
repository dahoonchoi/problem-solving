# Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

# aVeryBigSum has the following parameter(s):

# int ar[n]: an array of integers .

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    total = 0
    length = len(ar)
    
    for n in range(0,length):
        total += ar[n]
    
    return total
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(raw_input().strip())

    ar = map(long, raw_input().rstrip().split())

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()