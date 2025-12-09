
def plusOne(digits):
    _ = str(int(''.join([str(x) for x in digits])) + 1)
    return list(map(int, _))
    # return _digits

# digits = [1, 2, 3]
# digits = [4, 3, 2, 1]
digits = [9]
print(plusOne(digits))
