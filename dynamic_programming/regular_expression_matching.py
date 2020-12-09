
# you are given a regular expression and a string we need to check whether the regular expression 
# matches the string given 
# for the given problem
# "." ==> can match with any single character 
# "*" ==> can match with 0 or more characters before "*"

# sample test case 1
# regex: XA*B.C
# string: XAABYC



from collections import defaultdict
def match(regex, word):
    regex = " " + regex
    word = " " + word
    r = len(regex)
    s = len(word)
    dp = defaultdict(lambda:[False]*r)
    dp[0][0] = True # null character matches with null character

    for i in range(1, s):
        for j in range(r):
            
            # case 1: if the charecter matches with the regec, check whether diagnolly prev element is True
            if word[i] == regex[j]:
                if dp[i - 1][j - 1] == True:
                    dp[i][j] = True
                    continue
            # case 2:when regex character is ".", check whether the fidagnolly opposite element is True
            if regex[j] == ".":
                if dp[i - 1][j - 1] == True:
                    dp[i][j] = True
                    continue
            # case 3:when regex character is "*". check whether the j-2 element is matching withe the string chartacter
            if regex[j] == "*":
                # deleting all existence of the last element to * and checking the match
                if dp[i][j - 2] == True:
                    dp[i][j] = True
                    continue
                # checking the last elemnt matches with curent string element and checking till that element match exist
                if (regex[j - 1] == word[i] or regex[j - 1] == ".") and dp[i - 1][j] == True:
                    dp[i][j] = True
                    continue
    for i in dp.keys():
        print(dp[i])
    print(dp[s - 1][-1])



regex = input()
word = input()
match(regex, word)