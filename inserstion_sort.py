def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        # print(f"key-{key} and j-{j}")
        # print(f"arr-{arr}")
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            # print(f"arr-{arr}")
            j -= 1
        arr[j+1] = key
    return arr

arr = [50,40,60,30,5,3]
print(insertion_sort(arr))

# Note comments for debugging 