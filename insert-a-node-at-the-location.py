# Practice / Data Structures / Linked Lists / Insert a node at a specific position in a linked list

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

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    #create a new node
    node = SinglyLinkedListNode(data)
    
    if head == None: #if head pointer is NULL meaning that it's the first element
        head = node
    else:
        temp = head
        #skip the number of nodes to reach the position indicated by position argument
        count =1
        #while count<position and it is not out of bounds
        while temp!=None and count < position:  
            temp = temp.next #here we are iterating through the list
            count+=1
            
            #insert the node 
        
        node.next = temp.next #temp.next follows the new node
        temp.next = node #node follows the temp
    
    return head #return head because it iterates through the function multiple times =>
                #it will in agregate return multiple numbers
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
