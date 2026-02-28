def sub_array_with_sum(arr,target):
    start=0
    curr_sum=0

    for end in range(len(arr)):
        curr_sum += arr[end]

        #shrink window if sum exceeds target
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1

        if curr_sum==target:
            return arr[start:end+1]
    
    return None

arr = [1,2,3,7,5]
target = 15
print(sub_array_with_sum(arr, target))