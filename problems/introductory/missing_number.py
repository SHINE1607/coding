

def missing_number(n, arr):
    summation = n*(n + 1)/2
    missing = summation - sum(arr)
    print(int(missing))


n = int(input())
arr = input().split()
arr = [int(x) for x in arr]
missing_number(n, arr)