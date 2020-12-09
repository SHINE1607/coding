class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

#initiliising the linked list
# the head node wont contain any data, just the root node
class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        # on finding the last node
        cur.next = new_node
    
    def get_length(self):
        length = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            length += 1
        return length
    
    def display(self):
        current_node = self.head
        
        data_arr = []
        while current_node.next != None:
            current_node = current_node.next
            data_arr.append(current_node.data)
        print(data_arr)
             
            
    # get en alement at an index 
    def get_data(self, index):
        if index >= self.get_length():
            print("ERRROR: index out of bound")
            return None
        curr_node = self.head
        i = 0
        while curr_node != None:
            curr_node = curr_node.next
            if i == index:
                return curr_node.data
            i += 1
    # function to remove element at an index
    def remove(self, index):
        flag = 0
        if index >= self.get_length():
            print("ERRROR: index out of bound")
            return None 
        curr_node = self.head
        curr_index = 0
        while curr_node.next is not None:
            last_node =  curr_node
            curr_node = curr_node.next
            if curr_index == index:
                last_node.next = curr_node.next
                return " the item at {} has been removed".format(index)
            curr_index += 1





my_list = linked_list()
my_list.append(2)
my_list.append(10)
my_list.append(12)
my_list.append(21)
my_list.append(5)
my_list.append(7)
my_list.append(9)
my_list.append(99)
print(my_list.get_length())
my_list.display() 
print(my_list.get_data(3), "is the data at pos 3")
print(my_list.remove(4))
print(my_list.display())
        

        
        

