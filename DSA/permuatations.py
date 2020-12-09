from itertools import permutations
from collections import defaultdict
data = defaultdict(bool)
ans = []
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        global data, ans
        ans = []
        data = defaultdict(bool)
        # permu = list(permutations(nums, len(nums)))
        # ans = []
        # for i in range(len(permu)):
        #     permu[i] = list(permu[i])
        #     if permu[i] not in ans:
        #         ans.append(permu[i])
        # return(ans)
        
        self.rec(nums, [], 0)
        return(ans)
        
    
    
    def rec(self, arr, curr_arr, index):
        global data, ans
        if len(curr_arr) == len(arr):
            ans.append(curr_arr)
            return
        value = arr[index]
        temp = []
        for i in range(0, len(curr_arr) + 1):
            if i == 0:
                temp = [value] + curr_arr[i:]

            elif i == len(curr_arr):
                temp = curr_arr[:i] + [value]
            else:
                temp = curr_arr[:i] + [value] + curr_arr[i:]
            if data[str(temp)] == False:
                data[str(temp)] = True
                self.rec(arr,temp, index + 1)
            