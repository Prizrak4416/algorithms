def fast_s(array):
    if len(array) < 2:
        return array
    else:
        opor = array[0]
        left = [i for i in array[1:] if i <= opor]
        right = [i for i in array[1:] if i > opor]
        return fast_s(left) + [opor] + fast_s(right)


a = [3, 8, 3, 77, 33, 6, 99, 12]
print(fast_s(a))