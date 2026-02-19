def second_largest(arr):
    if len(arr)<2:
        return None

    if arr[0]>arr[1]:
        largest = arr[0]
        second_largest = arr[1]
    else:
        largest=arr[1]
        second_largest=arr[0]

    for i in range(2, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
        
    if largest == second_largest:
        return None   # No same second largest

    return second_largest


arr = [8, 3, 10, 7, 6]
print(second_largest(arr))


