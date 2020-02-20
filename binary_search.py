from math import ceil

def binary(mas, number):
    law = 0
    high = len(mas) - 1
    while law <= high:
        item = ceil((law + high) / 2)
        # item = (law + high) // 2 + (law + high) % 2
        check_number = mas[item]
        if check_number == number:
            return item
        elif check_number > number:
            high = item - 1
        else:
            law = item + 1
    return None

a = [x for x in range(1, 1000, 3)]

print(binary(a, 43))
