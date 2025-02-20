import sys
num=(sys.argv[1])
print(num)
print("sum of odd placed even digits is: ",sum([int(num[i]) for i in range(0,len(num),2)if int(num[i])%2==0]))
print("sum of odd placed odd digits is: ",sum([int(num[i]) for i in range(0,len(num),2)if int(num[i])%2==1]))
print("sum of even placed even digits is: ",sum([int(num[i]) for i in range(1,len(num),2)if int(num[i])%2==0]))
print("sum of even placed odd digits is: ",sum([int(num[i]) for i in range(1,len(num),2)if int(num[i])%2==1]))
n=int(num)
                                                                              