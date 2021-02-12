print('enter yor string')
a = list(map(int, input().split()))
a.sort()
i = 0
s = 0
f = 0
try:
    while i<len(a):
        if a[0] != 1:
            f = 1;
        else:
            f = a[len(a)-1]+1
        if a[i+1]-1 > a[i] and f!=1:
            s = a[i]+1
            break;
        i+=1
    print (s);
except IndexError:
    print(f)
