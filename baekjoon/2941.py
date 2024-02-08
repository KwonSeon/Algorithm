sentence = str(input())

alphabets = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for alphabet in alphabets:
	sentence = sentence.replace(alphabet, '*')
	# print(alphabet)

# print(sentence)
print(len(sentence))