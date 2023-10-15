def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0
    max=-1
    while i<len(data):
        if max<data[i]:
            if data[i]%2==0:
                max=data[i]
        i+=1
    return max
print(find_max_even([1, 4, 3, 8, 5]))
print(find_max_even([7, 6, 3, 4, 9]))