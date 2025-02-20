import sys
num=[int(i) for i in sys.argv[1:]]
def merge_sort_arr(num,low,high):
    if low<high:
        mid=(low+(high-low)//2)
        merge_sort_arr(num,low,mid)
        merge_sort_arr(num,mid+1,high)
        merge(num,low,mid,high)
def merge(num,low,mid,high):
    arr1=num[low:mid+1]
    arr2=num[mid+1:high+1]
    i,j=0,0
    k=low
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            num[k]=arr1[i]
            i+=1
        else:
            num[k]=arr2[j]
            j+=1
        k+=1
    num[k:high+1]=arr1[i:]+arr2[j:]
merge_sort_arr(num,0,len(num))
print(num)

