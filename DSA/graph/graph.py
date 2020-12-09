from collections import defaultdict
# time complexity :O(E + V)

class Graph:
    def __init__(self):
        self.graph  = defaultdict(list)


    def add_edge(self, parent, child):
        self.graph[parent].append(child)
        

    def dfs_rec(self, curr_node, visited):
        # addin the curr node to visited
        visited.add(curr_node)
        print(curr_node, end = " ")

        # iterting over all the nergbours of the curr node
        for neighbour in self.graph[curr_node]:
            if neighbour not in visited:
                self.dfs_rec(neighbour, visited)
            else:
                return


    def dfs(self, start):
        visited = set()

        self.dfs_rec(start, visited)
    visited = set
    def bfs(self, start):

        self.bfs_rec({start}, [start])
    
    

    def bfs_rec(self,visited, queue):
        if queue == []:
            print("")
            return
        first = queue.pop(0)
        print(first, end = " ")
        for neighbour in self.graph[first]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
        self.bfs_rec(visited, queue)


graph = Graph()
graph.add_edge(0, 7)
graph.add_edge(0, 9)
graph.add_edge(0, 11)
graph.add_edge(7, 3)
graph.add_edge(7, 6)
graph.add_edge(7, 11)
graph.add_edge(6, 5)

graph.add_edge(3, 4)
graph.add_edge(3, 2)

graph.add_edge(9, 8)
graph.add_edge(9, 10)

graph.add_edge(8, 1)
graph.add_edge(8, 12)

graph.add_edge(10, 1)

graph.add_edge(12, 2)



print("dfs", end= ": ")
graph.dfs(0)
print("")
print("bfs", end = ": ")
graph.bfs(0)