arr = [3, 4, 5, 6, 7, 8, 9]
start = 0
end = len(arr)-1

def binary_search(arr,start,end,search):
    if start <=end:
        mid = (start+end)//2
        if arr[mid] == search:
            return mid
        elif search < arr[mid] :
            return binary_search(arr,start,mid-1,search)
        elif search > arr[mid]:
            return binary_search(arr,mid+1,end,search)
    else:
        return -1
print(binary_search(arr,start,end,0))
# print(end)

