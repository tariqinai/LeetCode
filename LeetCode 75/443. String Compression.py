
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
count = 0
index = 0
ans = [chars[index]]

for i in range(len(chars)):
    if chars[index] == chars[i]:
        count += 1
    elif chars[index] != chars[i]:
        if count > 1:
            ans = ans + list(str(count))
        index = i
        ans.append(chars[index])
        count = 1
if count > 1:
    ans = ans + list(str(count))
chars[:] = ans

print(chars)
print(len(''.join(ans)))
