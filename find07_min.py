def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    i=0
    min=data[0]
    while i<len(data):
        if min>data[i]:
            min=data[i]
        i+=1
    return min
print(find_min([1, 2, -3, 4, 5]))
print(find_min([15, 23, 3, 9, 1, 4]))