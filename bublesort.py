#bublesort
a = [5,4,3,2,1,3,5]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)