def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    new = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
            
            
arr = [11,22,33,44,99,88,77,66,55,55,11]

print(merge_sort(arr))