def rotate_arr(arr,k):
    n=len(arr)

    k=k%n 
    rotated = arr[k:] + arr[:k]
    return rotated

arr=[1,2,3,4,5]
k=2

result=rotate_arr(arr,k)
print(result)
