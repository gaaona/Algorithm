word = input()

alphabet_dict = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

for char in word:
    if char.islower():
        char = char.upper()
    alphabet_dict[char] += 1

max_values = [k for k,v in alphabet_dict.items() if max(alphabet_dict.values()) == v]

if len(max_values) > 1:
    print('?')
else:
    print(max_values[0])