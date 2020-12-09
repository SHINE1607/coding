# itertaively increasing the reach  


# implmented using queue

# steps 
# we do the same steps as in dfs in here too but in a stack 
#  insetad of addinf the elements to the top of the stack, we add the children nodes top the end of the
# queue and pop out the firrt came lement in the queue

# so if we want print level by lebel we can use queue or bfs





class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child  = None

queue = []
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
            print(curr_node.value, end = " ")
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


    

    def level_order_traversal(self):
        global queue
        queue = []
        if self.root is None:
            return None
        else:
            queue.append(self.root.value)
            print("level_order_traversal:", end = " ")
            self.level_order_traversal_rec(self.root)


    def level_order_traversal_rec(self, curr_node):
        global queue
        print(queue[0], end = " ")
        queue = queue[1:]
        # if queue == []:
        #     print("\n")

        if curr_node.left_child is not None:
            queue.append(curr_node.left_child.value)
        if curr_node.right_child is not None:
            queue.append(curr_node.right_child.value)
        if curr_node.left_child is not None:
            self.level_order_traversal_rec(curr_node.left_child)
        if curr_node.right_child is not None:
            self.level_order_traversal_rec(curr_node.right_child)
        if len(queue) > 1:
            if queue[0] < queue[1]:
                print (" ")

        



    def size_rec(self, curr_node):
        if curr_node is None:
            return 0
        left_size =  self.size_rec(curr_node.left_child)
        right_size = self.size_rec(curr_node.right_child)
        return left_size + right_size + 1

    def size(self):
        print("Size of the tree: ",self.size_rec(self.root))



def fill_tree(tree, num_elems = 100, max_int = 100):
    from random import randint
    for i in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree



tree = binary_tree()
arr = [int(x) for x in input().split()]
for i in arr:
    tree.insert(i)

# tree = fill_tree(tree)
print("tree height:", tree.height())

# tree.search(200)
tree.inorder_traversal()
tree.level_order_traversal()
print(*queue)
# tree.size()