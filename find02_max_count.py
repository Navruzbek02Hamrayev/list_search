def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i=0
    max=data[0]
    while i<len(data):
        if max<data[i]:
            max=data[i]
        i+=1
    return data.count(max)
print(find_max_count([1, 8, 3, 8, 5]))
print(find_max_count([13, 8, 3, 4, 9]))
