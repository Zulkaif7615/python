def quick_sort(arr,left,right):
    if left < right:
        paivot = partition(arr,left,right)
        quick_sort(arr,left,paivot-1)
        quick_sort(arr,paivot+1,right)
        
        
def partition(arr,left,right):
    p = arr[left]
    i = left + 1
    j = right
    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[left],arr[j] = arr[j],arr[left]
    return j


arr = [77,55,4,77,3,2,55,77,88]

quick_sort(arr, 0, len(arr) - 1)
print(arr)