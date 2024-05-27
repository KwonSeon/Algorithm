import sys

input = sys.stdin.readline

N = int(input().strip())

M = int(input().strip())

amor = {}

materials = list(map(int, input().split()))

# print(materials)

ans = 0

while materials:
	material_number = materials.pop()
	target_number = M - material_number

	if target_number in  amor and amor[target_number] > 0:
		amor[target_number] -= 1
		ans += 1
	elif material_number not in amor:
		amor[material_number] = 1
	else:
		amor[material_number] += 1

print(ans)