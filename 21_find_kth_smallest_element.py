def kth_smallest(arr,k):
    arr.sort()
    return arr[k-1]

arr=[7,8,9,12,34,2]
k=3
print(kth_smallest(arr,k))