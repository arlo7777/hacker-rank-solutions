# Practice / Data Structures / Linked Lists / Insert a Node at the Tail of a Linked List

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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
singly_list = []
def insertNodeAtTail(head, data):
    #create a new node
    node = SinglyLinkedListNode(data)
     
    if head == None:
        head = node  #case1 : the head pointer is NULL
    else: #case2 : insert the node at the tail - creat a temp and traverse the list
        temp = head
        while temp.next != None:
            temp = temp.next  #the last element in the list = temp.next (the empty cell)
        
        temp.next = node   #now the last element of the list == the node passed in at                               the beginning of the function  
    return head #because we need to print an element of the list after each iteration 
    
    temp = head
    singly_list.append(temp.data)
    print(singly_list)
    temp = head.next()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
