def length(x):
    sum=0
    for i in range (103):
        if x[i]!=str('inf'): sum+=1
    return sum
