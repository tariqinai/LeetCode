
s='axc'
t='ahbgdc'
s_pointer = 0

if len(s) > 0:
    for char in t:
        if s_pointer >= len(s):
            print(True)
        elif char == s[s_pointer]:
            s_pointer += 1
if s_pointer == len(s):
    print(True)
else:
    print(False)
