# Practice / Tutorials / 30 Days of Code / Day 16: String to Integer 

import sys
S = input().strip()
try:
    print(int(S))
except ValueError:
    print("Bad String")
