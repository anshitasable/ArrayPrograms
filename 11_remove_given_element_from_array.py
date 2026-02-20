def remove_val(arr,val):
    k=0

    for i in range(len(arr)):
        if arr[i]!=val:
            arr[k]=arr[i]
            k+=1
    
    return arr[:k]

arr=[1,2,2,3,4,5]
val=2
print(remove_val(arr,val))