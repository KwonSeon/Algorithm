s = input().strip()

array = [s[i:] for i in range(len(s))]
array.sort(key=lambda x:x)

print(*array, sep='\n')