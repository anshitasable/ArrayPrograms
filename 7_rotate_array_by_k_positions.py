#Rotate the array to the right by k positions

def rotate_array(arr,k):
    n=len(arr)

    k=k%n   #handles if k>n

    rotated=arr[-k:]+arr[:-k]
    return rotated

arr=[1,2,3,4,5]
k=7

result=rotate_array(arr,k)
print(result)
