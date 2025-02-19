num_orange=int(input("enter the no of oranges: "))
stack=input().split()
stack=[int(i) for i in stack]
j=0
mid=stack[-1]
for i in range(num_orange-1):
    if stack[i]<mid:
        stack[i],stack[j]=stack[j],stack[i]
        j+=1
stack[j],stack[-1]=stack[-1],stack[j]
print(stack)






