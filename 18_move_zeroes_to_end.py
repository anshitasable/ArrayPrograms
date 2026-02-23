def move_zeroes_to_end(arr):
    pos=0

# moving all non zero elements forward
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos]=arr[i]
            pos+=1

# filling remaining positions with zero
    for i in range(pos,len(arr)):
        arr[i]=0
    return arr

arr=[1,0,0,0,4,5,0,2,0]
print(move_zeroes_to_end(arr))
    