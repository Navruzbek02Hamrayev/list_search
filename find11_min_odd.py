def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i=0
    min=data[0]
    while i<len(data):
        if data[i]%2==1:
            if min>data[i]:
                min=data[i]
        i+=1
    return min
print(find_min_odd([1, 8, 2, 8, 5]))
print(find_min_odd( [7, 8, 4, 3, 5]))

