def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    max=-1
    while i<len(data):
        if max<data[i]:
            if data[i]%2==1:
                max=data[i]
        i+=1
    return max
print(find_max_odd([1, 8, 3, 8, 5]))
print(find_max_odd([11, 7, 5, 4, 9]))