def hight_number(mas, i=0):
    if i < len(mas) - 1:
        maxim = hight_number(mas, i+1)
        if mas[maxim] < mas[i]:
            return i
        else:
            return maxim
    else:
        return i




arr = [5, 7, 3, 2, 6, 4, 7, 33, 12, 5]
print(hight_number(arr))