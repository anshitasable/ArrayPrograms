def sum_of_elements(arr):
    sum_=0

    for i in range(0,len(arr)):
        sum_=sum_+arr[i]
    return sum_

arr=[1,2,3,4,5]
sum_of_ele=sum_of_elements(arr)
print(f"The sum of elements is: {sum_of_ele}")    
