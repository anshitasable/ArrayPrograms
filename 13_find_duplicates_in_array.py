def find_duplicates(arr):
    seen=set()
    duplicates=set()

    for element in arr:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)

    return list(duplicates)


arr=[1,1,2,3,2,3,4,4,4,6,5,7]
print(find_duplicates(arr))