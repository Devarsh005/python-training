def bubble_sort(array):
    """bubble sort algorithm"""
    n = len(array)

    for i in range(1,n):
        for j in range(0,n-i):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]
    print(array)

numbers = [7,19,-3,4,0]
bubble_sort(numbers)