# Exercise itertools.product()

from itertools import product
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
L = list(product(l1, l2))
print(*L)

# Exercise itertools.permutations()

from itertools import permutations
n = list(input().split())
l = list(permutations(n[0], int(n[1])))
l.sort()
f = ""
for _ in l:
    for i in _:
        f += str(i)
    print(f)
    f = ""

# Exercise itertools.combinations()

from itertools import combinations
n = list(input().split())
l = list(n[0])
l.sort()
f = ""
for _ in range(0, int(n[1])):
    l1 = list(combinations(l, _+1))
    l1.sort()
    for i in l1:
        for p in i:
            f += str(p)
        print(f)
        f = ""

# Exercise itertools.combinations_with_replacement()

from itertools import combinations_with_replacement
n = list(input().split())
s = list(n[0])
s.sort()
l = list(combinations_with_replacement(s, int(n[1])))
l.sort()
f = ""
for _ in l:
    for i in _:
        f += str(i)
    print(f)
    f = ""

# Exercise Compress the String!

from itertools import groupby
L = []
n = str(input())
for k, v in groupby(n):
    L.append((len(list(v)),int(k)))
print(*L)

# Exercise  Iterables and Iterators

from itertools import combinations
N = int(input())
l = list(input().split())
K = int(input())
f = list(combinations(l,K))
count = 0
for _ in f:
    if "a" in _:
        count +=1
print(float(count/len(f)))

# Exercise Maximize It!

from itertools import product
n = list(map(int, input().split()))
K = n[0]
M = int(n[1])
l3 = []
fin = 0
for _ in range(0, K):
    l1 = list(map(int, input().split()))
    l2 = int(l1[0])
    l = l1[1:]
    l3.append(l)
x = lambda x : sum(i*i for i in x) % M
l4 = list(map(x, product(*l3)))
for _ in l4:
    if int(_) > fin:
        fin = _
print(fin)
