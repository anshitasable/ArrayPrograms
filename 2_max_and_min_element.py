
def find_max_min(arr):
    largest=arr[0]
    smallest=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    
        elif arr[i]<smallest:
            smallest=arr[i]
    
    return largest,smallest

arr=[8,3,10,7,6]
max_val, min_val = find_max_min(arr)

print(f"Largest element: {max_val}")
print(f"Smallest element: {min_val}")
