def pair_with_given_sum(arr,target):
    visited={}   

    for i in range(len(arr)):
        needed=target-arr[i]

        if needed in visited:
            return (needed,arr[i])      #pair found
        
        visited[arr[i]]=i    #store element after checking
    
    return None   #if pair not found

arr = [2, 7, 11, 15]
target = 9

result = pair_with_given_sum(arr, target)
print(result)