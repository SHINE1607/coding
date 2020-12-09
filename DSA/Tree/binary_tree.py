

from collections import defaultdict
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child  = None

arr = []
d = defaultdict(list)
class binary_tree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_rec(value, self.root)
    
    def insert_rec(self, value, curr_node):
        if curr_node.value == value:
            print("element cant be added")
            return 
        if value < curr_node.value:
            if curr_node.left_child == None:
                curr_node.left_child = Node(value)
                return
            else:
                self.insert_rec(value, curr_node.left_child )
        elif value > curr_node.value:
            if curr_node.right_child == None:
                curr_node.right_child = Node(value)
                return
            else:
                self.insert_rec(value, curr_node.right_child )
        
    def inorder_traversal_rec(self, curr_node):
        if curr_node is not None:
            self.inorder_traversal_rec(curr_node.left_child)
            print(curr_node.value)
            self.inorder_traversal_rec(curr_node.right_child)

        
    def inorder_traversal(self):
        if self.root == None:
            print("the tress is empty")
            return
        else:
            self.inorder_traversal_rec(self.root)

    def height_rec(self, curr_node, curr_height):
        if curr_node == None:
            return curr_height 
        left_height = self.height_rec(curr_node.left_child, curr_height + 1)
        right_height = self.height_rec(curr_node.right_child, curr_height + 1)
        return max(left_height, right_height)  
        
        
    def height(self):
        
        if self.root is not None:
            return self.height_rec(self.root, 0)
        else:
            return 0

    def search_rec(self, curr_node,value):
        if curr_node.value == value:
            print("Element found")
            return True
        elif value  > curr_node.value:
            if curr_node.right_child is not None:
                self.search_rec(curr_node.right_child, value)
            else:
                print("Element not found")
                return False
        elif value  < curr_node.value:
            if curr_node.left_child is not None:
                self.search_rec(curr_node.left_child, value)
            else:
                print("Element not found")
                return False
        

    def search(self, value):
        if self.root == None:
            print("The tree is empty")
            return False
        else:
            self.search_rec(self.root, value)

    queue = []

    def level_order_traversal_rec(self, curr_node):
        global queue
        print(queue[0], end = " ")
        queue = queue[1:]

        if curr_node.left_child is not None:
            queue.append(curr_node.left_child.value)
        if curr_node.right_child is not None:
            queue.append(curr_node.right_child.value)
        if curr_node.left_child is not None:
            self.level_order_traversal_rec(curr_node.left_child)
        if curr_node.right_child is not None:
            self.level_order_traversal_rec(curr_node.right_child)
        

    def level_order_traversal(self):
        global queue
        queue = []
        if self.root is None:
            return None
        else:
            queue.append(self.root.value)
            print("level_order_traversal:", end = " ")
            self.level_order_traversal_rec(self.root)

    def size_rec(self, curr_node):
        if curr_node is None:
            return 0
        left_size =  self.size_rec(curr_node.left_child)
        right_size = self.size_rec(curr_node.right_child)
        return left_size + right_size + 1

    def size(self):
        print("Size of the tree: ",self.size_rec(self.root))

    def level_order(self):
        global d
        matrix = []
        self.temp_rec( self.root, 0)

        for i in d.keys():
            print(*d[i])

    def temp_rec(self, curr_node, counter):
        global d
        if curr_node is None:
            return 
        else:
            d[counter].append(curr_node.value)
            self.temp_rec(curr_node.left_child, counter + 1)
            self.temp_rec(curr_node.right_child, counter + 1)

    def nodes_at_k_dist(self, k):
        global arr
        arr = []
        self.nodes_at_k_dist_rec(self.root, 0, k)
        print(arr)


    def nodes_at_k_dist_rec(self, curr_node, counter, k):
        global arr
        print(counter)
        if counter == k:
            if curr_node == None:
                return 
            else:
                arr.append(curr_node.value)
        else:
            if curr_node is not None:
                self.nodes_at_k_dist_rec(curr_node.left_child, counter + 1, k)
                self.nodes_at_k_dist_rec(curr_node.right_child, counter + 1, k)
            else:
                return

                


tree = binary_tree()
def fill_tree(tree, num_elems = 100, max_int = 100):
    from random import randint
    for i in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree




# arr = [int(x) for x in input().split()]
for i in arr:
    tree.insert(i)

tree = fill_tree(tree)
print("tree height:", tree.height())
tree.inorder_traversal()

# tree.search(200)
tree.level_order_traversal()
tree.size()
# tree.nodes_at_k_dist(2)
# tree.level_order()


# rememeber that dfs uses queue to traverse through nodes
# and bfs use a queue
