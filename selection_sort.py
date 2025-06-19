def selection_sort(arr):
    for i in range(len(arr)):
        print(f"for-i-{i}-arr{arr}")
        min_idx = i
        for j in range(i+1,len(arr)):
            print(f"arr[j]<arr[min_idx]")
            print(f"{arr[j]}<{arr[min_idx]}")
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
            print(f"for-j-{j}-arr{arr}")
    return arr 

arr = [5,7,3,12,8,4]
arr = [50,700,300,120,80,40]
print(selection_sort(arr))
         