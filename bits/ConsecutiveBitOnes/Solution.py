def longest_bit_run(n):
    longest_run = 0
    current_run = 0
    BITMASK = 1
    
    while n != 0:
        if n & BITMASK == 0:
            longest_run = max(longest_run, current_run)
            current_run = 0
        else:
            current_run += 1    
        n = n >> 1
    longest_run = max(longest_run, current_run)
    
    return longest_run

print(longest_bit_run(242))
# 4