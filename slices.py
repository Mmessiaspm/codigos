#slices
'''list = [10,8,6,4,2]
new_list = list[1:3]
print(new_list)'''
list = [12,3,11,5,1,9,7,15,13]
max = list[0]
min = list[0]
for i in list[1:]:
    if i>max:
        max=i
    else:
        if i<min:
            min=i    
print(max)
print(min)