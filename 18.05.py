
def func(tiv):
    type = "parz"
    for i in range(2, int(tiv/2)):
        if tiv % i == 0:
            type = "bard"
            break
        else:
            continue
    return type


print(func(int(input())))
