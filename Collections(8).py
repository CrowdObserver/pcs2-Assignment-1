# Exercise collections.Counter()

from collections import Counter
X = int(input())
l = list(map(int, input().split()))
N = int(input())
C = Counter(l)
count = 0
for _ in range(0, N):
    s = list(map(int, input().split()))
    if C[s[0]] > 0:
        count += s[1]
        C[s[0]] = C[s[0]] - 1
print(count)

# Exercise DefaultDict Tutorial

from collections import defaultdict
n, m = (input().split())
l = []
l1 = []
for _ in range(0, int(n)):
    l.append(input())
for _ in range(0, int(m)):
    l1.append(input())
s = []
for _ in l:
    ind = l.index(_)
    s.append((_, ind+1))
    l.remove(_)
    l.insert(ind,"BLANK")
d = defaultdict(list)
for key, value in s:
    d[key].append(value)
for _ in l1:
    if _ in d:
        print(*d.get(_))
    else:
        print("-1")

# Exercise Collections.namedtuple()

from collections import namedtuple
N = int(input())
x,y,z,w = input().split()
Marks = namedtuple("Marks",x+" "+y+" "+z+" "+w)
count = 0
for _ in range(0, N):
    l = list(input().split())
    tmp = Marks(l[0],l[1],l[2],l[3])
    count += float(tmp.MARKS)
print(float(count/N))

# Exercise Collections.OrderedDict()

from collections import OrderedDict
N = int(input())
k = 0
Dict = OrderedDict()
for _ in range(N):
    l = list(input().split())
    l1 = ""
    for i in l:
        if i.isdigit():
            k = int(i)
            l.remove(i)
    for i in l:
        l1 = l1 + i + " "
    l1 = l1[:-1]
    if l1 not in Dict:
        Dict[l1] = k
    else:
        Dict[l1] = Dict[l1] + k
for _ in Dict:
    print(_, Dict[_])

# Exercise Collections.deque()

from collections import deque
N = int(input())
d = deque()
for _ in range(N):
    i = list(input().split())
    if i[0] == "append":
        d.append(int(i[1]))
    elif i[0] == "pop":
        d.pop()
    elif i[0] == "appendleft":
        d.appendleft(int(i[1]))
    elif i[0] == "popleft":
        d.popleft()
print(*d)

# Exercise Company Logo

from collections import *
def mostLetters(s):
    l = []
    l1 = []
    for _ in s:
        l.append(_)
    C = Counter(l)
    f = dict()
    for k in C:
        if C[k] not in f:
            f[C[k]] = k
        else:
            f[C[k]] = f[C[k]] + k
    l2 = sorted(f.items())
    l2.reverse()
    for _ in l2:
        if len(_[1]) == 1:
            if len(l1) < 3:
                l1.append((sorted(_[1])[0], _[0]))
            else:
                break
        elif len(_[1]) == 2:
            if len(l1) < 3:
                l1.append((sorted(_[1])[0], _[0]))
                if len(l1) < 3:
                    l1.append((sorted(_[1])[1], _[0]))
            else:
                break
        elif len(_[1]) >= 3:
            if len(l1) < 3:
                l1.append((sorted(_[1])[0], _[0]))
                if len(l1) < 3:
                    l1.append((sorted(_[1])[1], _[0]))
                    if len(l1) < 3:
                        l1.append((sorted(_[1])[2], _[0]))
            else:
                break
        else:
            continue
    for _ in l1:
        print(_[0],_[1])

# Exercise Word Order

from collections import *
N = int(input())
l = []
for _ in range(N):
    s = input()
    l.append(s)
d = Counter(l)
print(len(d))
print(*d.values())

# Exercise Piling Up!

from collections import *
N = int(input())
for _ in range(N):
    res = "Yes"
    n1 = int(input())
    l = deque(map(int, input().split()))
    for i in reversed(sorted(l)):
        if i == l[0]:
            l.popleft()
        elif i == l[-1]:
            l.pop()
        else:
            res = "No"
            break
    print(res)