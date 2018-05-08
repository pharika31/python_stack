def push_front(arr, val):
    arr.append(val)
    arr[0], arr[len(x)-1] = arr[len(x)-1], arr[0]
    return arr
x = [1,2,3,4]
push_front(x ,5)
print x