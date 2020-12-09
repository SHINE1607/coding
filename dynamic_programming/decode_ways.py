# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.

 

# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

def numDecodings(s: str) -> int:
    dp = [0] * (len(s) + 1)
    
    dp[0] = 1
    if s[0] == "0":
        dp[0] = 1
    else:
        dp[1] = 1
    
    
    for i in range(2, len(s) + 1):
        # taking only the prev  digit
        op1 = int(s[i - 1])
        # considering the prev  and prev to prev digit
        op2 = int(s[i - 2] + s[i - 1])
        if op1 > 0:
            dp[i] += (dp[i - 1])
        
            
        if op2 >= 10 and op2 <= 26:
            dp[i] += dp[i - 2]
        
            
    return dp[-1]

print(numDecodings("225"))    

# the idea is that for each pos in the string we tak the  prev  one digit and 2 dgit and check for validity