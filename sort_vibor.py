def min_name(mas_values):
    min_n = mas_values[0]
    index_value = 0
    for value in range(1, len(mas_values)):
        if mas_values[value] < min_n:
            min_n = mas_values[value]
            index_value = value
    return index_value

def sort_mas_name(mas_values):
    sorted_mas = []
    for i in range(len(mas_values)):
        small_index = min_name(mas_values)
        sorted_mas.append(mas_values.pop(small_index))
    return sorted_mas

a = [5, 2, 88, 3, 74, 99, 4, 55]
b = ['fg', 'ty', 'uwoth', 'Adtrt', 'asdf']
print(sort_mas_name(a))
print(sort_mas_name(b))