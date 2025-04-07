def flattern_list(lst):
    i=0
    while i < len(lst):
        if isinstance(lst[i], list):
            lst[i:i +1]=lst[i]
        else:
            i += 1

list_1=[1, 2, 3, [4], [6, [7, [], 8, [9]]]]
flattern_list(list_1)
print(f"Flattern list: {list_1}")
