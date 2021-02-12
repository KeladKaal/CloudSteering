def fib(n):
    cur = 1
    old = 1
    i = 1
    while (i < n):
        cur, old, i = cur+old, cur, i+1
    return cur


print ("how many numbers do you want to get?")
n = int(input())
for i in range(n):
    print(fib(i))