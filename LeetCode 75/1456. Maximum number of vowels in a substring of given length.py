
s = 'abciiidef'
k = 3
vowels = {'a', 'e', 'i', 'o', 'u'}
j, curr, res = 0, 0, 0

for i in range(len(s)):
    curr += 1 if s[i] in vowels else 0
    if i-j+1 > k:
        curr -= 1 if s[j] in vowels else 0
        j += 1
    res = max(curr, res)
print(res)