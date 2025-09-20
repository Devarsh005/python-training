array = [20,10,12,-30,-9,1600,-15,0]

def merge_sort(array):
    size = len(array)
    if size > 1:
        half = size//2
        left = array[:half]
        right = array[half:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
                k += 1
            else:
                array[k] = right[j]
                j += 1
                k += 1
        # if left side array elements are remainig then 
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        # if right side of elements are remaining
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        return array
arr = merge_sort(array)
print(f"sorted arr -> {arr}")


