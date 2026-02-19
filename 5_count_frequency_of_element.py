def count_freq(arr):

    freq={}

    for element in arr:
        if element in freq:
            freq[element]+=1
        else:
            freq[element]=1
        
    return freq

arr=[1,2,2,3,1,1,4,5,4]
result=count_freq(arr)
print(result)