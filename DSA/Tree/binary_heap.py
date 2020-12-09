import copy

# Min heap
# getting the minimum number: O(1)
# removal: O(logn)
# insertion: O(logn)
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value 
        self.left = left
        self.right = right


class min_heap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root.value = value
            return
        else:
            self.insert_rec(self.root, value)

    def insert_rec(self, curr_node, value):
        if curr_node is None:
            curr_node = Node(value)
            return 
        else:
            if curr_node.val > value:
                if curr_node.left !=  None:
                    if curr_node.left.val < value:        
                        new_node = Node(value)
                        new_node.left = curr_node.left
                        curr_node.left = new_node
                        return
                    else:
                        self.insert_rec(curr_node.left, value)
                        self.insert_rec(curr_node.right, value)
                else:
                    new_node = Node(value)
                    curr_node.left = new_node
                    return
                if curr_node.right is not None:

                
            else:
                new_node = Node(value)
                temp_node = copy.copy(curr_node)
                curr_node 
        



heap1 = min_heap()





