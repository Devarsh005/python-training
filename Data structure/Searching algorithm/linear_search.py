numbers = [-12, 5, 11, 22, 25, 34, 64, 90]
search = 64
def linear_search(arr):
    for index,element in enumerate(arr):
        if element == search:
            return f"{element} at index {index}"
    else:
        return f"not found"
print(linear_search(numbers))