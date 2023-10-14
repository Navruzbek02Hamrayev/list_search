def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i=0
    min=data[0]
    while i<len(data):
        if min>data[i]:
            min=data[i]
        i+=1
    return data.count(min)
print(find_min_count([1, 8, 3, 8, 5]))
print(find_min_count([0, -4, 3, 9, -2, -4]))
