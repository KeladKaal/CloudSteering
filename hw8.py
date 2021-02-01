s = input()
while s != 'cancel':
    if s.isdigit():
        if int(s) % 2 == 0:
            print (int(s)//2)
        else:
            print (int(s)*3+1)
    else:
        print('Failed to convert text to number.')
    s = input()
print ('Bye!')