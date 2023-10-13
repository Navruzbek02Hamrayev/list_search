def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i=0
    max=data[0]
    while i<len(data):
        if max<data[i]:
            max=data[i]
        i+=1
    return max
print(find_max([1, 2, 3, 4, 5]))
print(find_max([12, 2, 5, 2, 7, 9, 1]))
    