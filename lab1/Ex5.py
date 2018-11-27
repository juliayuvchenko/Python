array = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
flat_list = []


def make_list_flat(array, flat_list):
    if isinstance(array, list):
        for x in array:
            if isinstance(x, list):
                make_list_flat(x, flat_list)
            else:
                flat_list.append(x)


make_list_flat(array, flat_list)
print("Flat list: %s" % flat_list)