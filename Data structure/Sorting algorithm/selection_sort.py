data = [25,15,-9,0,8,6]

def selection_sort(data):
    size = len(data)
    for i in range(size):
        minimum = i
        for next in range(i+1,size):
            if data[next] < data[minimum] :
                minimum = next
        data[i] ,data[minimum] = data[minimum] , data[i]
    print(data)
selection_sort(data)
