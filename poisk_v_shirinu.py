from collections import deque


def shirin(graf, val):
    result = {}
    result[val] = 0
    deq = deque([val])
    while deq:
        prov = deq.popleft()
        for n in graf[prov]:
            if n not in result:
                result[n] = result[prov] + 1
                deq.append(n)
    return result


a = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: [6, 3], 6: []}
print(shirin(a, 1))