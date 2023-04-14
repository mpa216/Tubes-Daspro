def length(x):
    sum=0
    for i in range (103):
        if x[i]!=str('inf'): sum+=1
    return sum

def mappend(arr, c):
    new_arr = [None] * (length(arr) + 1)
    for i in range(length(arr)):
        new_arr[i] = arr[i]
    new_arr[length(arr)] = c
    return new_arr
