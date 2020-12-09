from collections import Counter


def palindrome_reorder(string):
    if len(string) == 1:
        print(string)
        return
    counter = Counter(string)
<<<<<<< HEAD
    freq_arr = list(counter.values()).sort(reverse = True)
    if freq_arr[-1]%2 == 1 and freq_arr[-2]%2 == 1:
        print("NO SOLUTION")
        return
=======
    freq_arr = list(counter.values())
    odd_count = 0
    for i in freq_arr:
        if i%2 == 1:
            odd_count += 1
            if odd_count >= 2:
                print("NO SOLUTION")
                return
>>>>>>> f55fdab3c6ded2513a158623af13d93c09e5e1a3
    res = list(counter.keys())[-1] * freq_arr[-1]
    for i in list(counter.keys())[:-1]:
        res += i*int(counter[i]/2)
        res = i*int(counter[i]/2) + res
        
    print(res)
    return





string = input()
palindrome_reorder(string)