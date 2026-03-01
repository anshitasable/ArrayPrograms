def all_subarrays(arr):
    n=len(arr)

    for i in range(n): #starting index
        for j in range(i,n): #ending index
            print(arr[i:j+1])

arr=[8,9,10,11]                  #total subarrays=n(n=1)/2
all_subarrays(arr)