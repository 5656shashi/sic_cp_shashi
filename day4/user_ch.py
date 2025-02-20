import sort
arr=list(map(int, input().split()))
ch=input("enter the sorting algorithm u want to use: ")[0].lower()
if ch=='i':
    print(sort.insertion_sort(arr))  
elif ch=='m':
    sort.merge_sort_arr(arr,0,len(arr))
    print(arr)
elif ch=='q':
    sort.quick_sort(arr, 0, len(arr)-1)
    print(arr)
elif ch=='b':
    sort.bubble_sort_arr(arr)
    print(arr)
else:
    print("enter correctly")

