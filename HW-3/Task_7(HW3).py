def merge_sorted_list(list_a, list_b):
    sorted_list=[]
    x, y=0,0

    while x < len(list_a) and y < len(list_b):
        if list_a[x] < list_b[y]:
            sorted_list.append(list_a[x])
            x+=1
        else:
            sorted_list.append(list_b[y])
            y+=1

    while x < len(list_a):
        sorted_list.append(list_a[x])
        x+=1

    while y < len(list_b):
        sorted_list.append(list_b[y])
        y+=1
    
    return sorted_list

list_1=[5, 6, 8, 55, 78]
list_2=[5,7,9,11,45]
print(merge_sorted_list(list_1, list_2))



    
    