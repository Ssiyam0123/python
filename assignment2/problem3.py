def findDuplicates(lst):
    duplicates = []
    for i in lst:
        if lst.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates 

givenList = [1, 5, 6, 5, 1, 2, 3]

result = findDuplicates(givenList)

print(result)
