amount = int(input("Enter the amount: "))
deno_list = list(map(int,input("Enter note values: ").split()))
deno_list.sort(reverse = True)
for note in deno_list:
    number = amount // note
    print("No of",note,"'s is :",number)
    amount = amount % note
