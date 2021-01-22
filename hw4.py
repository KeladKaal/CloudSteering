print ('enter yor string')
a = list(input())
sum = 0
whole_sum=0
for i in a:
    if i.isdigit():
     sum = sum*10+float(i)
    else:
     whole_sum+=sum
     sum = 0
whole_sum+=sum
print (whole_sum)
