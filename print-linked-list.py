# Practice / Data Structures / Linked Lists / Print the Elements of a Linked List

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):

    temp = head  #we need this to create a temporary pointer 
    
    while temp!=None:
        print(temp.data)   #print data that belongs to this head
        temp=temp.next       #go to the next head until the head == None  
    
if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
