from itertools import permutations
def creating_strings(string):
    permu = list(set(permutations(string, r = len(string))))
    print(len(permu))
    permu.sort()
    for i in permu:
        print("".join(i))

string = input()
creating_strings(string)