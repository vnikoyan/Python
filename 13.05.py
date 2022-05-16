'''
def func(x, y):
    if x>y:
        print(x)
    else:
        print(y)
x = int(input("enter number 1 ------"))

y = int(input("enter number 1 ------"))
func(x,y)
'''
num = str(input())


for i in range(0 , len(num)):
    if num[i] == "+":
        print(int(num[0 : i])+int(num[(i+1) : len(num)]))
    elif num[i] == "-" and i == 0:
        print(-int(num[0 : i])-int(num[(i+1) : len(num)]))
    elif num[i] == "*":
        print(int(num[0 : i])*int(num[(i+1) : len(num)]))
    elif num[i] == "/":
        print(int(num[0 : i])/int(num[(i+1) : len(num)]))
