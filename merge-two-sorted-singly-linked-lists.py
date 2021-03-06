# Practice / Data Structures / Linked Lists / Merge two sorted linked lists

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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
import sys
sys.setrecursionlimit(100000)

def mergeLists(head1, head2):
    
    #case1: both lists are NULL 
    
    if head1 == None and head2 == None:
        return None
    
    #case2: one list is NULL 
    
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    
    #algorithm
    
    if head1.data < head2.data:
        #create a temp variable 
        temp = head1
        temp.next = mergeLists(head1.next, head2) #temp.next = the minimum of the minimum of the next two numbers head1.next and head2
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next) #mergeLists is a recursive function we pass the values into  
    
    return temp
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
