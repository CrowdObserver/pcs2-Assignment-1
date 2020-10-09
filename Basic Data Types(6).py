# Exercise Find the Runner-Up Score!


def runner_up(l):
    l = set(l)
    l = list(l)
    l.sort()
    return l[-2]


# Exercise Lists

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(0, N):
        s = list(input().split())
        if s[0] == "insert":
            l.insert(int(s[1]), int(s[2]))
        elif s[0] == "remove":
            l.remove(int(s[1]))
        elif s[0] == "print":
            print(l)
        elif s[0] == "append":
            l.append(int(s[1]))
        elif s[0] == "pop":
            l.pop()
        elif s[0] == "reverse":
            l.reverse()
        elif s[0] == "sort":
            l.sort()

# Exercise Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = ()
    for _ in integer_list:
        t = t + (_,)
    print(hash(t))

# Exercise Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    p = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for _ in student_marks[query_name]:
        p += float(_)
    print(format(p/3,".2f"))

# Exercise List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = []
    for _ in range(0, x+1):
        for i in range(0,y+1):
            for s in range(0, z+1):
                a = int(_)
                b = int(i)
                c = int(s)
                if a+b+c != n:
                    l.append([a,b,c])
    print(l)

# Exercise Nested Lists

if __name__ == '__main__':
    students = []
    k = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    for i in students:
        k.append(i[1])
    k.sort()
    g = k[0]
    for el in k:
        if float(g) < float(el):
            g = float(el)
            break
    fin = []
    for _ in students:
        if _[1] == g:
            fin.append(_[0])
            fin.sort()
    for _ in fin:
        print(_)