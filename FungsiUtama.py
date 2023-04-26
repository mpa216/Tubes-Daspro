import random

def length(x):
    i, sum=0,0
    while i!=103:
        if x[i]!=str('inf'): sum+=1
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

def extract(idxcolumn, namaf) :

    # Open the CSV file in read mode
    with open(namaf, 'r') as file:

        # Read all the lines from the file
        lines = file.readlines()

        # Initialize an empty list to store the ids
        items = []

        # Loop over the lines starting at index 1
        for i in range(1, len(lines)):
            # Split the line using the comma separator
            columns = my_split(lines[i], ",")
            
            # Extract the value of the id column (first column)
            item = (columns[idxcolumn])
            
            # Append the id to the ids list
            items = mappend(items, item)
        return items
    
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

def update_bahan(pasir, batu, air) :
    # Open the CSV file in read mode
    with open('bahan_bangunan.csv', 'r') as file:
        
        # Read all the lines from the file
        lines = file.readlines()

        # Loop over the lines and concatenate the values in the jumlah column
        for i in range(1, len(lines)):
            columns = my_split(lines[i], ",")
            if columns[0] == 'pasir':
                columns[2] = str(pasir) + '\n'
            elif columns[0] == 'batu':
                columns[2] = str(batu) + '\n'
            elif columns[0] == 'air':
                columns[2] = str(air)

            # Concatenate the columns using a loop
            line = ''
            for j in range(len(columns)):
                if j < len(columns) - 1:
                    line += columns[j] + ','
                else:
                    line += columns[j]

            # Replace the line in the file with the updated line
            lines[i] = line

    # Open the CSV file in write mode
    with open('bahan_bangunan.csv', 'w') as file:
        
        # Write the updated lines to the file
        file.writelines(lines)

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

def update_hapus(arr) :
    # Open the CSV file in read mode
    with open('hapus.csv', 'r') as file:
        # Read all the lines from the file
        lines = file.readlines()

    # Open the CSV file in write mode to overwrite the values
    with open('hapus.csv', 'w') as file:
        # Write the header line
        file.write('id')

        # Loop over the values in the array and write them to the file
        for i in range(len(arr)):
            file.write('\n' + str(arr[i]))
