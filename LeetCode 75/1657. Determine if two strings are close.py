
from collections import defaultdict, Counter

word1 = "cabbba"
word2 = "abbccc"
# word1 = 'kyq'
# word2= 'kqy'
word1Dict = Counter(word1)
word2Dict = Counter(word2)

# print(set(word1) == set(word2))
# print(set(word1), set(word2))

if len(word1) != len(word2):
    print(False)
print((set(word1) == set(word2)) and (Counter(word1Dict.values()) == Counter(word2Dict.values())))

# else:
#     for i in range(len(word1)):
#         word1Dict[word1[i]] += 1
#         word2Dict[word2[i]] += 1
#
#     if (word1Dict.keys() == word2Dict.keys()) and (sorted(list(word1Dict.values())) == sorted(list(word2Dict.values()))):
#         print(True)
#     else:
#         print(False)

# print(word1Dict)
# print(word2Dict)