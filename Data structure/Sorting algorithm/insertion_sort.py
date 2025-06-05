def insertion_sort(array):
    size = len(array)
    for i in range(1,size):
        key = i
        for j in range(i-1,-1,-1):
            if array[key] < array[j]:
                array[key] , array[j] = array[j] , array[key]
                key -=1
            elif array[key] > array[j]:
                break
    return array

# array
array = [64, 34, 25, -12, 22, 11, 90, 5]
print(f"sorted array is {insertion_sort(array)}")