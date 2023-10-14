def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0
    max=data[0]
    while i<len(data):
        if data[i]%2==0:
            if max<data[i]:
                max=data[i]
        i+=1
    return max
print(find_max_even([1, 4, 3, 8, 5]))
print(find_max_even([7, 6, 3, 4, 9]))