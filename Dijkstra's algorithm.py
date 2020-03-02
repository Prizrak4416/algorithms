def find_min(mincos, check):
    min = float('inf')
    num = None
    for key, value in mincos.items():
        if value < min and key not in check:
            min = value
            num = key
    return num


def dejkstor(graph):
    costs = graph['start']
    parents = (lambda x: {key: 'start' for key in costs.keys()})(costs)
    costs['finish'] = float('inf')  # beskonechnost
    processed = []  # obrabotannie
    min_cos = find_min(costs, processed)
    while min_cos != None:
        cost = costs[min_cos]
        neighbors = graph[min_cos]
        for key in neighbors.keys():
            new_costs = cost + neighbors[key]
            if key not in costs.keys():
                costs[key] = new_costs
                parents[key] = min_cos
            if costs[key] > new_costs:
                costs[key] = new_costs
                parents[key] = min_cos
        processed.append(min_cos)
        min_cos = find_min(costs, processed)
    puti(parents, costs)
    return parents


def puti(parents, costs):
    nach = 'finish'
    mass = [nach]
    while parents[nach] != 'start':
        nach = parents[nach]
        mass.append(nach)
    mass.append('start')
    mass.reverse()
    print(mass)
    print('max time -', costs['finish'])

arr = {'start': {'a': 6, 'b': 2, 'c': 2}, 'a': {'finish': 1}, 'b': {'a': 3, 'finish': 5}, 'c': {'b': 1, 'e': 1, 'finish': 5}, 'e':{'finish': 1},  'finish': {}}
print(dejkstor(arr))