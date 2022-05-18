
def func(tiv):
    type = "parz"
    for i in range(2, int(tiv/2)+1):
        if tiv % i == 0:
            type = "bard"
            break
        else:
            continue
    return type


n = int(input())
for tiv in range(2, n):
    res = func(tiv)
    if res == "parz":
        print(tiv)
