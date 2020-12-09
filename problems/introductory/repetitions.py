

def repetitions(string):
    longest = 1
    curr_long = [string[0]]
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            curr_long.append(string[i])
            
        else:
            if len(curr_long) > longest:
                longest = len(curr_long)
            curr_long = [string[i]] 
    print(max(len(curr_long), longest))
string = input()
repetitions(string)