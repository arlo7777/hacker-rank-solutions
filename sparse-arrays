# Practice / Data Structures / Arrays / Sparse Arrays

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    new_dict = Counter(strings)         #new dict with key: strings, value: count 
    result = []
    for i in queries:                #for item in queries check if 
        result.append(new_dict[i])            #the item is in the existing dictionary, and what is its count 
    return result                                      #return the list of the counts 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
