# TODO: implement LL methods as built-ins class __method__ (magic methods) if applicable


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
        node = self.head
        pre = self.head

        # loop to assign last (node.next == None)
        while node.next:
            pre = node
            node = node.next
        # assign previous as last & decrease list len
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1

        # case: list might consist of one Node
        if self.lenght == 0:
            self.head = None
            self.tail = None
        
        return node
    
    def prepend(self, value):
        self.new_node = Node(value)
        # case: empty list
        if self.lenght == 0:
            self.head = self.new_node
            self.tail = self.new_node
        else:
            self.new_node.next = self.head
            self.head = self.new_node
        self.lenght += 1

        # not important
        return True

    def pop_first(self):
        if self.lenght == 0:
            return None
        
        # self.head - we want to return
        # assign self.head to new one
        node = self.head
        self.lenght -= 1

        if self.lenght == 0:
            self.head = None
            self.tail = None
        else:
            self.head = node.next

        node.next = None
        return node
    
    # index methods should raise IndexError instead of None
    def get_value(self, index):
        # index means the number of node; LL doesn't have arrays' like indexes
        if index < 0 or index >= self.lenght:
            raise IndexError('Index {} is out of range.'.format(index))

        # start from head to find on index
        node = self.head

        for _ in range(index):
            node = node.next
        return node
    
    def set_value(self, index, value):
        node = self.get_value(index)      
        node.value = value
        return True
    
    def insert(self, index, value):
        # validate index value and find node on prev index, 
        # to get prev node and link it with a new one

        # cases to insert as a first node/last node <- assuming we reset head/tail
        if index == 0:
            return self.prepend(value)
        
        pre_node = self.get_value(index - 1)

        if not pre_node.next:
            return self.append(value)
        
        node_to_move = pre_node.next
        new_node = Node(value)

        pre_node.next = new_node
        new_node.next = node_to_move
        return True

    def remove(self, index):
        # IndexError if not index
        node = self.get_value(index)

        try:
            pre_node = self.get_value(index - 1)
        except IndexError:
            # node we got - the first node: reset head pointer to node.next
            self.head = node.next
                
            if node.next == None:
                self.tail == None
        else:
            pre_node.next = node.next

        node.next = None
        self.lenght -= 1

        return node
    
    def remove_(self, index):
        """
        Implements approach from the course.

        P.S. Don't like it, coz rep of logic in .get_value()
        """

        if index < 0 or index >= self.lenght:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.lenght - 1:
            return self.pop()
        pre_node = self.get_value(index - 1)
        node = pre_node.next
        pre_node.next = node.next
        node.next = None
        self.lenght -= 1
        return node

    def reverse(self):
        """
        head->[11]->[3]->[23]->[7]->None<-tail to 
        tail->None<-[11]<-[3]<-[23]<-[7]<-head
        """
        # 1. reverse head and tail
        node = self.head
        self.head = self.tail
        self.tail = node
        # node.next = None
        pre_node = None
        next_node = node.next
        # 2. move pre_node, node, next_node in loop (for/while): 
        # links next.next to node, node.next to pre etc.
        for _ in range(self.lenght):
            next_node = node.next
            node.next = next_node
            # 3. there's a gab between node and next_node
            pre_node = node
            node = next_node


linked_list = LinkedList(4)

linked_list.append(6)
linked_list.append(8)
linked_list.append(10)
linked_list.append(12)


linked_list.print_list()
