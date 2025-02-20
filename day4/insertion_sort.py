import sys
arr=[int(i) for i in sys.argv[1:]]
print(arr)
def insertion_sort(arr):
    sarr=[]
    sarr.append(arr[0])
    for i in arr[1:]:
        j=0
        while j<len(sarr) and i>sarr[j]:
            j+=1
        sarr.insert(j,i)
    return sarr
print(insertion_sort(arr))
    
         

    