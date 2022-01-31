class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.lenght = 1

    def print_list(self):
        temp = self.head

        while temp != None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        self.new_node = Node(value)

        if not self.head:
            self.head = self.new_node
            self.tail = self.new_node
        else:
            self.tail.next = self.new_node
            self.tail = self.new_node

        self.lenght += 1

        # not important
        return True
    
    def pop(self):
        # if empty list
        if self.lenght == 0:
            return None
        
        # iter over list to find last and previous; previous will be assigned as the last
        # last points to None; both start from the beggining
        temp = self.head
        pre = self.head

        # loop to assign last (node.next == None)
        while temp.next:
            pre = temp
            temp = temp.next
        # assign previous as last & decrease list len
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1

        # case: list might consist of one Node
        if self.lenght == 0:
            self.head = None
            self.tail = None
        
        return temp
    
    def prepend(self, value):
        self.new_node = Node(value)
        # case: empty list
        if self.lenght == 0:
            self.head = self.new_node
            self.tail = self.head
        else:
            self.new_node.next = self.head.next
            

        self.lenght += 1

        # not important
        return True


linked_list = LinkedList(4)
print('Head:', linked_list.head.value)
print('Tail:', linked_list.tail.value)
print('Len:', linked_list.lenght)

linked_list.append(6)
linked_list.append(8)
linked_list.append(10)
linked_list.append(12)

linked_list.print_list()

print('Head:', linked_list.head.value)
print('Tail:', linked_list.tail.value)
print('Len:', linked_list.lenght)

print('Poped item:', linked_list.pop().value)
print('Poped item:', linked_list.pop().value)
