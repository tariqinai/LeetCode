
my_dict = {}


def longest_common_prefix(strs):
    prefix = ''

    for i in range(len(strs[0])):
        for s in strs:
            if i==len(s) or s[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    return ''.join(prefix)

my_strs = ["flower","flow","flight"]
my_strs = ["dog","racecar","car"]
print(longest_common_prefix(my_strs))
