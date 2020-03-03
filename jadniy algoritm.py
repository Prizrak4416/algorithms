def jadniy(sellers, needs):
    best_seller = None
    final_seller = set()
    best_needs = set()
    while needs:
        for key, value in sellers.items():
            proverka = needs & value
            if len(proverka) > len(best_needs):
                best_seller = key
                best_needs = value
        needs -= best_needs
        best_needs = set()
        final_seller.add(best_seller)
    return final_seller


seller = {}
seller['vasia'] = set(['apple', 'orange', 'bananas'])
seller['shurik'] = set(['carrot', 'cabbage', 'apple'])
seller['arra'] = set(['carrot', 'orange', 'bananas', 'mandarin'])
seller['tutik'] = set(['mandarin', 'apple', 'potatoes', 'cabbage', 'tomato'])
seller['bandit'] = set(['orange', 'mandarin', 'tomato'])

need = set(['apple', 'mandarin', 'orange', 'orange'])

print(jadniy(seller, need))
