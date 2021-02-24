# problem 6
print(sum([f for f in range (101)])**2 - sum([i*i for i in range (101)]))

# problem 9
print([(x*y*(x**2 + y**2)**(0.5)) for x in range (400) for y in range(300) if (x+y+(x**2+y**2)**0.5 == 1000 and x != 0 and y != 0)])

# problem 48
print(str(sum([i**i for i in range (1, 1001)]))[-10:])

# problem 40
from functools import reduce
print(reduce(lambda x, y: x * y,[int("".join([str(x) for x in range(10000001)])[10**z]) for z in range(7)]))
