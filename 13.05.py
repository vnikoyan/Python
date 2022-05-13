mylist = [21, -9, 15, 2116, -71, 33]
number = int(input("enter tiv"))
list = []
for item in mylist:
    list.append(abs(item-number))
print(list.index(min(list)))
