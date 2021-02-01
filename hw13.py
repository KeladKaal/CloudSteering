def degrees(a, s):
    if s == "c":
        print ((a*1.8)+32)
    elif s == "f":
        print ((a-32)/1.8)
    else:
        print ("wrong enter")


print("enter degrees")
a = int(input())
print ("if in celsius then write с if in fahrenheit then f")
s = input()
degrees(a, s)

