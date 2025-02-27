
s = "leet**cod*e"
stack = []
# s = "erase*****"
# i = 0
# s_list = list(s)
#
# while i < len(s_list):
#     if s_list[i] == '*':
#         s_list.pop(i)
#         s_list.pop(i-1)
#         i -= 1
#     else:
#         i += 1
#
# print(''.join(s_list), s_list)

for val in s:
    if val == '*':
        stack.pop()
    else:
        stack.append(val)
print(''.join(stack))