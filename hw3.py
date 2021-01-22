print ('enter yor string')
a = list(input().split())
a = [x.lower() for x in a]
#enter string and downgrade

my_dict = {i:a.count(i) for i in a}
abc =  max(my_dict, key=my_dict.get)
#find the biggest key

for key in my_dict:
    if my_dict.get(key) == my_dict.get(abc):
     print(key, my_dict.get(key))
#print values with these keys