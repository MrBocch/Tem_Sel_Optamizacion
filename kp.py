# unbounded KP
class Item:
    def __init__(self, weight, profit):
      self.weight = weight
      self.profit = profit

    def __str__(self):
        return f"Beneficio: {self.profit} - Peso: {self.weight}"

    def __repr__(self):
        return f"P: {self.profit} W: {self.weight}"

# Max profit heuristic, spam sack with item with most profit
def MaxP(items, capacity):
    sorted_items = sorted(items, key=lambda item: (-item.profit, item.weight))
    sack = []
    sack_total_weight = 0
    for item in sorted_items:
        while sack_total_weight + item.weight <= capacity:
            sack_total_weight += item.weight
            sack.append(item)

    return sack

# Min weight heuristic, spam sack with item with least weight ratio
def MinW(items, capacity):
    sorted_items = sorted(items, key=lambda item: (item.weight, -item.profit))
    sack = []
    sack_total_weight = 0
    for item in sorted_items:
        while sack_total_weight + item.weight <= capacity:
            sack_total_weight += item.weight
            sack.append(item)
        # podemos salir de lopp porque sabemos que no existe otro
        # item con un peso menos que el primero
        break

    return sack

def MaxPW(items, capacity):
    sorted_items = sorted(items, key=lambda item: item.profit/item.weight, reverse=True)
    sack = []
    sack_total_weight = 0
    for item in sorted_items:
        while sack_total_weight + item.weight <= capacity:
            sack_total_weight += item.weight
            sack.append(item)

    return sack

def instance_profit(items):
    return sum([i.profit for i in items])

def bruteforce(items, capacity):
    def  knapsack_recursive(items, capacity, index, selected_items):
        if index >= len(items) or capacity == 0:
            return selected_items

        # Case 1: Skip the current item
        without_item = knapsack_recursive(items, capacity, index + 1, selected_items[:])

        # Case 2: Take the current item (if it fits)
        with_item = []
        if items[index].weight <= capacity:
            with_item = knapsack_recursive(
                items, capacity - items[index].weight, index, selected_items + [items[index]]
            )

        # Return the list corresponding to the better choice
        return with_item if sum(item.profit for item in with_item) > sum(item.profit for item in without_item) else without_item

    return knapsack_recursive(items, capacity, 0, [])

CAPACITY = 50
# Item(WEIGHT, PROFIT)
items = [
    Item(10, 16),
    Item(6, 10)
]
# heuristics
# MaxP
# MinW
# MaxPW
# bruteforce
pf = MaxPW(items, CAPACITY)
pf_profit = instance_profit(pf)

print(pf)
print(pf_profit)
