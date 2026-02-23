def are_equal(arr1,arr2):
    if len(arr1)!=len(arr2):
        return False

    freq={}

    for num in arr1:
        freq[num]=freq.get(num,0)+1

    for num in arr2:
        if num not in freq or freq[num]==0:
            return False
            freq[num]-=1
    return True

arr1=[4,3,2,1,1]
arr2=[1,2,3,4]
print(are_equal(arr1,arr2))