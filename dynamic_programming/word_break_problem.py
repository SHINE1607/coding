# given a string such and a distionary of words, check whether the string can be split into words in the dictioanry

# dp[i][j] = Bool value whether word[:i] can be string in distionary
from collections import defaultdict




def word_break(words, string):
    dp = defaultdict(lambda:[False]*(len(string)))

    # loop to itertate over upper diagonal matrix
    for length in range(len(string)):
        i = 0
        while i + length < len(string):

            if length == 0: # if charecter length = 0, they can be checked direclty
                if string[i] in words:
                    dp[i][i + length] = True 
                i += 1
                continue

            # coindition if teh word itself is in the dictionary 
            if string[i:i + length + 1] in words:
                dp[i][i + length] = True
            # if not, checking whether we can split the string into words in the dictionary 
            else:
                for j in range(i + 1, i + length + 1):
                    if dp[i][j - 1] == True and dp[j][i + length] == True:
                        dp[i][i + length] = True  
                        break
            i += 1


    print(dp[0][-1])


words = input().split()
string =  input()
word_break(words, string)
