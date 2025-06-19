def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"i-{i}-arr-{arr}")
        for j in range(n-i-1):
            print(f"arr[j]<arr[j+1]")
            print(f"{arr[j]}>{arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print(f"j-{j}-arr-{arr}")
    return arr

arr = [70,60,50]
print(bubble_sort(arr))