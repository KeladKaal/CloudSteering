print('enter yor string')
a = list(map(int, input().split()))
a.sort()
i = 0
while i<len(a):
    if a[i+1]-1 > a[i]:
        s = a[i]+1
        break;
    i+=1
print (s);