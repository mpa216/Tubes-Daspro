def length(x):
    sum=0
    for i in range (103):
        if x[i]!=float('inf'): sum+=1
    return sum

def mappend(arr, c):
    new_arr = [None] * (length(arr) + 1)
    for i in range(length(arr)):
        new_arr[i] = arr[i]
    new_arr[length(arr)] = c
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
            new_arr.append(arr[i])
    return new_arr

def my_max(seq):
    if len(seq) == 0:
        raise ValueError("max() arg is an empty sequence")
    else:
        max_val = seq[0]
        for val in range(len(seq)):
            if seq[val] > max_val:
                max_val = seq[val]
        return max_val

def my_min(seq):
    if len(seq) == 0:
        raise ValueError("min() arg is an empty sequence")
    else:
        min_val = seq[0]
        for val in range(len(seq)):
            if seq[val] < min_val:
                min_val = seq[val]
        return min_val
