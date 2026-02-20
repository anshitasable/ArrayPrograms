def remove_duplicates(arr):
    seen=set()
    result=[]

    for element in arr:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result

arr = [1, 2, 2, 3, 1, 4, 5, 4]
print(remove_duplicates(arr))

