def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle_of_list=len(lst)//2
    left_half=lst[:middle_of_list]
    right_half=lst[middle_of_list:]

    sorted_left_half=merge_sort(left_half)
    sorted_right_half=merge_sort(right_half)

    return merge_sorted_list(sorted_left_half, sorted_right_half)

def merge_sorted_list(list_a, list_b):
    sorted_list=[]
    x,y=0,0

    while x < len(list_a) and y < len(list_b):
        if list_a[x] <= list_b[y]:
            sorted_list.append(list_a[x])
            x+=1
        else:
            sorted_list.append(list_b[y])
            y += 1

    while x < len(list_a):
        sorted_list.append(list_a[x])
        x += 1
    
    while y < len(list_b):
        sorted_list.append(list_b[y])
        y += 1
    
    return sorted_list

unsorted_list = [8, 3, 5, 4, 6, 2, 7, 1]
print(merge_sort(unsorted_list))

    