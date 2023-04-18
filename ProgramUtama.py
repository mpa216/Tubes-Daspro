def length(x):
    i, sum=0,0
    while i!=103:
        if x[i] != str('inf'): sum+=1
        i +=1
    return sum

def mappend(arr, c):
    new_arr = [None] * (length(arr) + 1)
    for i in range(length(arr)):
        new_arr[i] = arr[i]
    new_arr[length(arr)] = c
    return new_arr
