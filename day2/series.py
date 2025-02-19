def if_prime(number):
    for i in range(2,number):
        if number%i==0:
            return 0
    return number
def fibo_series(n):
    a=1
    b=2
    if n==1:
        return a
    elif n==2:
        return b
    else:
        i=0
        sum=0
        while i<n-2:
            i+=1
            sum=a+b
            a=b
            b=sum
        return sum
def prime_Series(n):
    i=0
    j=2
    while i<n:
        res=if_prime(j)
        if res!=0:
            i+=1
        j+=1
    return res
term=int(input("enter the term of the series: "))
if term %2==0:
    print(prime_Series(term/2))
else:
    print(fibo_series((term//2)+1))

        

