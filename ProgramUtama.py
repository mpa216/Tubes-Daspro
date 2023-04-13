usernamejin = [] # array ini isinya string
passwordjin = [] # array ini isinya string
jenisjin = [] # 0: pengumpul 1: pembangun, array ini isinya integer
usernamelain = ["Bandung", "Roro"]
passwordlain = ["Bondowoso", "Jonggrang"]
IDcandi = [] # Ini array 2 dimensi ex. [[12fd, 3de, 4aa], [2sa, 1we], [1gf], ...] isinya string
bahancandi = [] # Ini array 2 dimensi ex. [[120, 200, 300], [50, 20 , 200] ...] isinya integer dengan format [[pasir, air, batu]]
useraktif = [] # array ini isinya string ex. "Bandung"



def length(x):
    i, sum=0,0
    while i!=103:
        if x[i]!=str('inf'): sum+=1
        i+=1
    return sum

def mappend(arr, c):
    new_arr = [None] * (length(arr) + 1)
    for i in range(length(arr)):
        new_arr[i] = arr[i]
    new_arr[length(arr)] = c
    return new_arr
