word1 = 'abcde'
word2 = 'pqr'
final = ''

if len(word1) > len(word2):
    for i in range(len(word2)):
        final = final + word1[i] + word2[i]

    final = final + word1[len(word2):]

elif len(word1) < len(word2):
    for i in range(len(word1)):
        final = final + word1[i] + word2[i]

    final = final + word2[len(word1):]

else:
    for i in range(len(word1)):
        final = final + word1[i] + word2[i]

print(final)
