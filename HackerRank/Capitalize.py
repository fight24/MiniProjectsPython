s = "12pham phuong"


def solve(s):
    lst = []
    for c in s.split():
        if c.isalpha():
            lst.append(c.capitalize())
        else:
            lst.append(c)
    return (" ".join(lst)).strip()


print(solve(s))