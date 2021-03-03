# Practice / Data Structures / Arrays / Array Manipulation

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #initialize array with zeroes
    # [0,0,0 ... x n times] we need 1D array because the function updates the same array
    
    array = [0] * (n+2) #(n+2) because we start from index1 and update 1 index past n
    
    for a, b, k in queries:
        array[a]+=k
        array[b+1]-=k
               
    maxnumber = temp = 0
    
    for value in array:
        temp+=value
        #after iteration through each array maxnumber saves the maximum number
        maxnumber=max(maxnumber, temp) 
    
    return maxnumber


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
