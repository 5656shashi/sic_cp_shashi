def partion_array(numbers, low, high):
    j = low
    pivot = numbers[high]
    for i in range(low, high):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i] # move the smaller element to the left
            j += 1
    numbers[j], numbers[high] = numbers[high], numbers[j] # place the pivot element in its final position
    return j
def quick_sort(numbers, low, high):
    if low < high:
        pivot_index = partion_array(numbers, low, high)
        quick_sort(numbers, low, pivot_index-1)
        quick_sort(numbers, pivot_index+1, high)


def insertion_sort(arr):
    sarr=[]
    sarr.append(arr[0])
    for i in arr[1:]:
        j=0
        while j<len(sarr) and i>sarr[j]:
            j+=1
        sarr.insert(j,i)
    return sarr

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

def bubble_sort_arr(arr):
    for i in range(len(arr)-1):
        s=True
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                s=False
        if s:
            return 



