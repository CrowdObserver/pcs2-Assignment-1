# Exercise Set.add()

n = int(input())
s = set()
for _ in range(0, n):
    s.add(input())
print(len(s))

# Exercise Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
n1 = int(input())
for _ in range(0, n1):
    j = list(map(str, input().split()))
    if len(j) >= 2:
        j2 = int(j[1])
    else:
        j2 = 0
    if j[0] == "pop":
        s.pop()
    elif j[0] == "remove":
        s.remove(j2)
    elif j[0] == "discard":
        s.discard(j2)
count = 0
for _ in s:
    count += int(_)
print(count)

# Exercise Set.union() Operation

n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))
print(len(s1 | s2))

# Exercise Set.intersection() Operation

n = int(input())
s1 = set(map(int, input().split()))
n_ = int(input())
s2 = set(map(int, input().split()))
print(len(s1 & s2))

# Exercise Set.difference() Operation

n3 = int(input())
s1 = set(map(int, input().split()))
n4 = int(input())
s2 = set(map(int, input().split()))
print(len(s1 - s2))

# Exercise Set.symmetric_difference() Operation

n5 = int(input())
s1 = set(map(int, input().split()))
n6 = int(input())
s2 = set(map(int, input().split()))
print(len(s1 ^ s2))

# Exercise Symmetric Difference

n7 = int(input())
s1 = set(map(int, input().split()))
n8 = int(input())
s2 = set(map(int, input().split()))
s4 = s1 - s2
s5 = list(s4.union(s2 - s1))
s5.sort()
for _ in s5:
    print(_)

# Exercise Set Mutations

n = int(input())
sA = set(map(int, input().split()))
n_sets = int(input())
s5 = 0

for _ in range(0, n_sets):
    j2 = list(map(str, input().split()))
    if j2[0] == "intersection_update":
        a = set(map(int, input().split()))
        sA.intersection_update(a)
    elif j2[0] == "update":
        b = set(map(int, input().split()))
        sA.update(b)
    elif j2[0] == "difference_update":
        c = set(map(int, input().split()))
        sA.difference_update(c)
    elif j2[0] == "symmetric_difference_update":
        d = set(map(int, input().split()))
        sA.symmetric_difference_update(d)

for _ in sA:
    s5 += int(_)
print(s5)

# Exercise Check Subset

nT = int(input())
for i in range(0, nT):
    n1T = int(input())
    sA = set(map(int, input().split()))
    n2T = int(input())
    sB = set(map(int, input().split()))
    if sB.union(sA) == sB:
        print(True)
    else:
        print(False)

# Exercise Check Strict Superset

sA = set(map(int, input().split()))
nN = int(input())
var = True
for _ in range(0, nN):
    sB = set(map(int, input().split()))
    for i in sA.symmetric_difference(sB):
        if i in sB:
            var = False
print(var)


# Exercise Introduction to Sets

def average(array):
    s = set(array)
    count = 0.0
    for _ in s:
        count += float(_)
    return float(count) / float(len(s))


# Exercise The Captain's Room

K = int(input())
l = list(map(int, input().split()))
sA = set()
sCap = set()
for _ in l:
    if _ not in sA:
        sA.add(_)
    else:
        sCap.add(_)
print(sA.difference(sCap).pop())

# Exercise No Idea!

nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
s = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for _ in s:
    if _ in A:
        happiness += 1
    elif _ in B:
        happiness += -1
    else:
        happiness += 0
print(happiness)