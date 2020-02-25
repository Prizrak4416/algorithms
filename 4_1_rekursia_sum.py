def sum_rek(mas):
    if len(mas) == 0:
        return 0
    else:
        return mas.pop(0) + sum_rek(mas)


arr = [4, 7, 3, 2, 6, 4, 7]
print(sum_rek(arr))
