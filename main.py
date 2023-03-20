"""Module takes in array input and returns sorted squared array output"""
def sorted_squared_array(array):
    """
    function returns sorted squared array
    """
    newarray = [x*x for x in array]
    newarray.sort()
    return newarray

if __name__ == "__main__":
    """"""
    arr = [1, 2, 3, 5, 6, 8]
    out = sorted_squared_array(arr)
    print(arr)
