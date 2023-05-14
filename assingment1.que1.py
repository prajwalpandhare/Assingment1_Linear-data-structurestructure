##Q1: Define Node class to represent a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Define Linked List class to represent the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
    # add a node to the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    # print the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()

    # delete elements in linked list whose sum is zero
    def delete_zero_sum(self):
        temp = self.head
        sum_list = {}
        total_sum = 0
        while temp is not None:
            total_sum += temp.data
            if total_sum == 0:
                self.head = temp.next
                sum_list.clear()
            elif total_sum in sum_list:
                sum_list[total_sum].next = temp.next
            else:
                sum_list[total_sum] = temp
            temp = temp.next

# test the program with a sample input
llist = LinkedList()
llist.append(6)
llist.append(4)
llist.append(-3)
llist.append(-4)
llist.append(3)
llist.append(10)
llist.append(2)
llist.append(5)
llist.append(-5)
llist.print_list()
llist.delete_zero_sum()
llist.print_list()