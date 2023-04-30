def length(x):
    sum=0
    for i in range (102):
        if x[i]!=['inf','inf','inf']: sum+=1
    return sum

def mappend(arr, c):
    new_arr = [None] * (length(arr) + 1)
    for i in range(length(arr)):
        new_arr[i] = arr[i]
    new_arr[length(arr)] = c
    return new_arr
def append_lain(arr,c):
    newarr = arr
    for i in range (2,102):
        if arr[i]==['inf','inf','inf']:
            newarr[i]=c
            break
    return newarr
