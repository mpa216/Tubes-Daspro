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
