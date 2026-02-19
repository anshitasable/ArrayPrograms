def array_is_sorted(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            print("Array is not sorted")
            return False
    
    print("Array is sorted")
    return True


arr = [5,3,8,6,7,1]
result = array_is_sorted(arr)
