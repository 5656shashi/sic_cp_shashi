import sys
arr=[int(i) for i in sys.argv[1:]]
def bubble_sort_arr(arr):
    for i in range(len(arr)-1):
        s=True
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                s=False
        if s:
            return 
bubble_sort_arr(arr)
print(arr)
