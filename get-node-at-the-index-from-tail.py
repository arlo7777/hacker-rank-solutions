# Practice / Data Structures / Linked Lists / Get Node Value

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail): #gives an index from tail 
    #initialize two pointers 
    temp1 = head
    temp2 = head
    
    #traverse to the position from the head
    for i in range(positionFromTail):
        temp1 = temp1.next
    
        #traverse both pointers 
        #this is clever because temp1 and temp2 will be apart from each other
        #as if temp1 is the tail and temp2 is the node at the desired position
        #this works because they will always have the distance of (0, position)
        #meaning that once temp1 reaches the end of the list, temp2 will be
        #exactly positionFromTail apart from it and return that value 
        #we don't need to sybtract -1 from positionFromTail because 0th position is the tail and we start from 0th index
    while temp1.next!=None:
        temp1 = temp1.next
        temp2 = temp2.next
        
    return temp2.data

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()
