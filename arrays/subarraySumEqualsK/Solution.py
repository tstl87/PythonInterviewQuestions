
def find_continuous_k(l, k):
    previous_sums = {0:-1}
    s = 0
    for index, n in enumerate(l):
        s += n
        previous_sums[s] = index
        if previous_sums.get(k):
            return l[:index+1]
        if( previous_sums.get(s-k) and previous_sums[s-k] != -1):
            #return previous_sums
            return l[ previous_sums[s-k]+1: index+1 ]
    return None
    
print(find_continuous_k([1, 3, 2, 5, 7, 2], 6))