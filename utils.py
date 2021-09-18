import random
from tabulate import tabulate


def get_sample(min_, max_, cantidad):
    return [random.randint(min_, max_) for i in range(cantidad)]

def print_table(data, headers):
    array_from_arrays = []
    for d in data:
        array = []
        for k, v in d.items():
            array.append(v)
        array_from_arrays.append(array)

#    print(array_from_arrays)
    print (tabulate(array_from_arrays, headers=headers))