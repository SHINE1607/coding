# given n keys and cost associated with it, find the optimal tree to have minum cots to search for a key
# total numnber trees possible fiir n keys: 2nCn/(n + 1)
# average comparsion is caluculated by (number of levels)/no of leaf nodes

# total cost is calculated by cost of (leaf node * level)

# imf the cost is not there, hi=eght balanced tree wouuld have the least cost


# dp state: dp[i][j] = cost of searching nodees from i to j

#  we take all the possibluties of keys by considering only tne uppper diagnal matrix


from collections import defaultdict

def optimal(n,data, cum_weights):

    dp =defaultdict(lambda:[1e7 + 9]*(n))

    for diff in range(0, n):
        i = 0
        while i + diff < n:
            if diff == 0:
                dp[i][i + diff] = data[i][1]
                i += 1
                continue

            # we have to take all nodes from i to i + diff as the root node
            for j in range(i, i + diff + 1):

                # for each node we have to select the most optimal left branch and right branch
                # and we selct the node having the most optimal left and right branch
                if j == i:  # codittion when we the root node is left most element
                    left = 0
                    right = dp[j+1][i + diff]
                elif j == i + diff: # codittion when we the root node is right most element
                    right = 0
                    left = dp[i][j - 1]
                else:   # normal case
                    left = dp[i][j- 1]
                    right = dp[j + 1][i + diff]
                    
                # print("******", i, i + diff, "****")
                # print(left, right)
                # taking the minimum value from taking all nodes
                dp[i][i + diff] = min(dp[i][i + diff], left + right + cum_weights[i + diff + 1] - cum_weights[i])
            
            
            i += 1
        
    print(dp[0][diff]), 




n = int(input())
keys = [int(x) for x in input().split()]
costs = [int(x) for x in input().split()]
data = list(zip(keys, costs))

data.sort()
cum_weights = [0]*n
for i in range(n):
    cum_weights[i] = data[i][1] + cum_weights[i-1]
cum_weights = [0] + cum_weights
optimal(n, data, cum_weights)



