
s = "race a car"

# Solution 1
# s = list(s)
# vowels = 'aeiouAEIOU'
# temp = {}
#
# for i, vowel in enumerate(s):
#     if vowel in vowels:
#         temp[i] = vowel
#
# reverse_dict = list(reversed(temp.keys()))
#
# for i, (_, value) in enumerate(temp.items()):
#     s[reverse_dict[i]] = value

# print(''.join(s))

# Solution 2
s = list(s)
vowels = 'aeiouAEIOU'
i, j = 0, len(s)-1

while i<j:
    if s[i] not in vowels:
        i +=1
    elif s[j] not in vowels:
        j -= 1
    else:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

print(''.join(s))
