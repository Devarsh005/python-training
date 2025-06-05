def bubble_sort(array):
    """bubble sort algorithm"""
    n = len(array)

    for i in range(1,n):
        for j in range(0,n-i):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]
    return array

numbers = [7,19,-3,4,0]
print(f" sorted list is: {bubble_sort(numbers)}")