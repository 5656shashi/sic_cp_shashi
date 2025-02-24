t=int(input("Enter the no of test cases: "))
res_list = []
for i in range(t):
    n=int(input("Enter the no of students girls or boys: "))
    boys = list(map(int,input("Enter the height of boys: ").split()))
    girls = list(map(int,input("Enter the height of girls: ").split()))
    order=boys+girls
    order.sort()
    res = True
    for i in range(0,n*2,2):
        if order[i]in boys and order[i+1]in girls:
            pass
        else:
            res = False
    if not res:
        for i in range(0,n*2,2):
            if order[i]in girls and order[i+1]in boys:
                res = True
            else:
                res = False
    if res:
        res_list.append("YES")
    else:
        res_list.append("NO")
    
for i in res_list:
    print(i)
