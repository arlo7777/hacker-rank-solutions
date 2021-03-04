# Practice / Data Structures / Linked Lists / Delete a Node

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

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    #if we must delete the first node then simply make the head node equal head.next
    if position == 0:
        head = head.next
    else:
        temp = head #need a temp variable to be able to traverse the list independently                       of its initial node aka head
        count = 1
        while temp != None and count < position: #this will continue traversing unless
        #temp reaches the end of the list or the given position
        
        #now we need to delete the node by modifying the links of it to the next node
            temp = temp.next #this is how we traverse the list until count<position
            count+=1 #must keep track of the count 
    
        #now that we are at the right position and ready to delete the node, proceed 
        #the pointer is at the node that preceeds the node we want to delete
        
        temp.next = temp.next.next #break the link between temp and temp.next
    return head
    
       
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
