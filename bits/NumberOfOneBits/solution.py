def one_bits(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n = n >> 1
    return count

print(one_bits(23))
# 0b10111