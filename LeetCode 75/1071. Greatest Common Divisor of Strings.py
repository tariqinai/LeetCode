
str1 = 'ABCABC'
str2 = 'ABC'
substr = ''

len1, len2 = len(str1), len(str2)

for i in range(len1, 0, -1):
    substr = str1[:i]
    temp1 = int(len1/i)
    temp2 = int(len2 / len(substr))
    if (substr * temp1 == str1) and (substr * temp2 == str2):
        print("GCD: ", substr)
        break
    else:
        print(substr)
        substr = ''


print("Final :", substr)
