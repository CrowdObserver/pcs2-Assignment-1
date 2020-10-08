# Exercise What's Your Name?


def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")


# Exercise String Split and Join

def split_and_join(line):
    a = line
    a = a.split(" ")
    a = "-".join(a)
    return a


# Exercise sWAP cASE

def swap_case(s):
    g = ""
    for i in s:
        if i == i.upper():
            g += i.lower()
        else:
            g += i.upper()
    return g


# Exercise Mutations

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = "".join(string)
    return string


# Exercise Find a string

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string) is True:
            count += 1
    return count


# Exercise String Validators

def isString(s):
    a = False
    b = False
    c = False
    d = False
    e = False
    for i in s:
        if i.islower():
            a = True
            if i.isalnum():
                e = True
                if i.isdigit():
                    c = True
                elif i.isalpha():
                    d = True

        elif i.isupper():
            b = True
            if i.isalnum():
                e = True
                if i.isdigit():
                    c = True
                elif i.isalpha():
                    d = True
        elif i.isdigit():
            c = True
            e = True
        else:
            None
    print(e)
    print(d)
    print(c)
    print(a)
    print(b)


# Exercise Capitalize!

def solve(s):
    s = s.split(" ")
    k = ""
    for i in s:
        if i != "":
            i = i[0].upper() + i[1:len(i)]
            k = k + " " + i
        else:
            k += " "
    s = k[1:]
    return s


# Exercise Text Wrap

def wrap(string, max_width):
    k = 0
    if str(float(len(string)) / float(max_width)).isdigit():
        k = len(string) / max_width
    else:
        k = int(float(len(string)) / float(max_width)) + 1
    result = ""
    for i in range(0, k):
        result += string[:max_width] + "\n"
        string = string[max_width:]
    return result


# Exercise String Formatting

def print_formatted(number):
    k = len(str(bin(number))[2:])
    for i in range(0, number):
        print((str(i + 1).rjust(k) + str(oct(i + 1))[2:].rjust(k + 1) + str(hex(i + 1))[2:].upper().rjust(k + 1) + str(
            bin(i + 1))[2:].rjust(k + 1)))


# Exercise Merge The Tools!

def merge_the_tools(string, k):
    l = list(string)
    l1 = []
    l2 = []
    fin = ""
    fin1 = ""
    for j in range(0, int(len(string) / k)):
        for i in l:
            l1 = l[:k]
        for g in l1:
            if g not in l2:
                l2.append(g)
        for i in l2:
            fin += str(i)
        fin1 += fin + "\n"
        fin = ""
        l = l[k:]
        l2 = []
    print(fin1)
