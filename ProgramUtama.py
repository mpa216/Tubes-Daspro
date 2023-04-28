from FungsiLogin import login

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
def append_lain(arr,c):
    for i in range (2,103):
        if arr[i]==['inf','inf','inf']:
            arr[i]==c
    return arr

arrUser = [[float('inf')for j in range (3)]for i in range (103)]
arrUser[2] = ['jin','pass','Pembangun']
arrUser[0] = ["Bandung","cintaroro","bandung_bondowoso"]
arrUser[1] = ["Roro","cintaroro","gasukabondo"]
useraktif = ""
roleaktif = ""


useraktif,roleaktif = login(arrUser,useraktif,roleaktif)
print(useraktif,roleaktif)
