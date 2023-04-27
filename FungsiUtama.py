import random

def length(x):
    i, sum=0,0
    while i!=103:
        if x[i]!=str('inf'): sum+=1
        i+=1
    return sum

def lengthcandi(x):
    i, sum=0,0
    while i!=100:
        if x[i][0]!=str('inf'): sum+=1
        i+=1
    return sum

def mappend(arr, c):
    new_arr = [None] * (len(arr) + 1)
    for i in range(len(arr)):
        new_arr[i] = arr[i]
    new_arr[len(arr)] = c
    return new_arr

def my_split(string, delimiter=None):
    result = []
    current_word = ""
    if delimiter is None:
        delimiter = " "
    for i in range(len(string)):
        char = string[i]
        if char == delimiter:
            if current_word:
                result = mappend(result, current_word)
                current_word = ""
        else:
            current_word += char
        if i == len(string) - 1:
            result = mappend(result, current_word)
    return result

def del_element(arr, index):
    new_arr = []
    for i in range(len(arr)):
        if i != index:
            new_arr = mappend(new_arr, arr[i])
    return new_arr

    
def my_max(seq):
    if len(seq) == 0:
        raise ValueError("max() arg is an empty sequence")
    else:
        max_val = int(seq[0])
        for val in range(len(seq)):
            if int(seq[val]) > max_val:
                max_val = int(seq[val])
        return max_val

def my_min(seq):
    if len(seq) == 0:
        raise ValueError("min() arg is an empty sequence")
    else:
        min_val = int(seq[0])
        for val in range(len(seq)):
            if int(seq[val]) < min_val:
                min_val = int(seq[val])
        return min_val


def my_sort(arr):
    # Iterate over each element of the array
    for i in range(len(arr)):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
