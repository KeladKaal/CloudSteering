def collatz(a, n):
    if a==1:
        print(n)
    else:
        if a%2 == 0:
            collatz(a/2, n+1)
        else:
            collatz(a*3+1, n+1)

a = int(input())
n = collatz(a, 0)


