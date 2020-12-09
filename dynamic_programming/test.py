from collections import defaultdict

def letterCombinations(digits):
    
    dict_data = defaultdict(str)
    string = sorted("qwertyuiopasdfghjklzxcvbnm")
    for i in range(2, 10):
        if i == 7 or i == 9:
            dict_data[str(i)] = string[:4]
            string = string[4:]
        else:
            dict_data[str(i)] = string[:3]
            string = string[3:]
        
    if len(digits) == 0:
            return []
    curr_ans = dict_data[digits[0]]    
    first = dict_data[digits[0]]   
    for i in range(1, len(digits)):
        
        curr_ans = []
        for j in first:
            temp = [j] * len(dict_data[digits[i]])
            curr_ans += list(zip(temp, list(dict_data[digits[i]])))
            
            
            # print(ans)
        curr_ans = ["".join(x) for x in curr_ans]
        first = curr_ans
    print(curr_ans)
                

letterCombinations("2")