# Exercise Mod Divmod

n = int(input())
m = int(input())
print(divmod(n,m)[0])
print(divmod(n,m)[1])
print(divmod(n,m))

# Exercise Power - Mod Power

a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))

# Exercise Integers Come In All Sizes

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a,b)+pow(c,d))

# Exercise Polar Coordinates

from cmath import *
n = complex(input())
print(abs(n))
print(phase(n))

# Exercise Triangle Quest 2

for i in range(1, int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)**2)

# Exercise Triangle Quest

for i in range(1, int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**(i)//9)*i)

# Exercise Find Angle MBC

import math
AB = int(input())
BC = int(input())
AC = math.hypot(AB,BC)
res = round(math.degrees(math.acos(BC/AC)))
print(res, end="")
print(chr(176), end="")