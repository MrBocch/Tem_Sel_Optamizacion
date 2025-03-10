from itertools import permutations

def calculate_distance(route, distances):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1)) + distances[route[-1]][route[0]]

def tsp_brute_force(distances):
    n = len(distances)
    cities = list(range(n))
    min_distance = float('inf')
    best_route = None

    for perm in permutations(cities):
        dist = calculate_distance(perm, distances)
        if dist < min_distance:
            min_distance = dist
            best_route = perm

    return best_route, min_distance

def tsp_brute_force_directed(distances):
    n = len(distances)
    cities = list(range(n))
    min_distance = float('inf')
    best_route = None

    for perm in permutations(cities):
        dist = calculate_distance(perm, distances)
        if dist < min_distance:
            min_distance = dist
            best_route = perm

    return best_route, min_distance

Inf = float("inf")

# Just change this
distances = [
    [0, 10, 30, 40],
    [10, 0, 15, 18],
    [30, 15, 0, Inf],
    [40, 18, Inf, 0]
]

#tsp_brute_force(distances)
# tsp_brute_force_directed(distances)

#route, distance = tsp_brute_force_directed(distances)
route, distance = tsp_brute_force(distances)
print("Best route:", route)
print("Minimum distance:", distance)
