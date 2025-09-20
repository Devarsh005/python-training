# size = len(data)
# low = 0
# pivot = data[-1]
# i = 0
# for index in range(i,size-1):
#     if data[index] < pivot :
#         # swap if element is less than pivot
#         data[i],data[index] = data[index] , data[i]
#         i += 1
# else:
#     data[i],data[-1] = pivot , data[i]
# print(data)


def partition(data,low,high):
    pivot = data[low]
    i = low
    j = high
    while i < j:
        while data[i] <= pivot and i<=high:
            i += 1
        while data[j] >pivot and j>=low:
            j -= 1
        if i < j:
            data[i] , data[j] = data[j] , data[i]
    data[low] , data[j] = data[j], data[low]
    return j
def quick_sort(data,low,high):
    if low < high:
        j = partition(data,low,high)
        quick_sort(data,low,j)
        quick_sort(data,j+1,high)


data = [90,15,-30,20,-34,10,40,400]
size = len(data)
quick_sort(data,0,size-1)
print(data)
# print(pivot)
# print(size)
# print(low)