from itertools import combinations

N, M = map(int, input().split())

# city = [input() for _ in range(N)]
city = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
# 	print(city[i])

houses = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]
chicken_houses = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]

# print(f'houses: {houses}')
# print(f'chicken_houses: {chicken_houses}')

comb_chicken = combinations(chicken_houses, M)

# print(f'comb_chicken: {list(comb_chicken)}')


def distance(combination):
	return sum(min(abs(hy - cy) + abs(hx - cx) for cy, cx in combination) for hy, hx in houses)


min_distance = min(distance(comb) for comb in comb_chicken)

print(min_distance)