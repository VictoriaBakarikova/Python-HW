def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def uniq_elements(list_i):
    flat_list = flatten_list(list_i)
    set_of_uniq = set(flat_list)
    return set_of_uniq


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(uniq_elements(list_a))
