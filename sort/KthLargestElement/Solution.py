def findKthLargest(nums, k):
    return sorted(nums)[len(nums) - k]
    # Time complexity O(n*log(n))
    # Space complexity O(log(n))


def findKthLargest2(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]
    # Time complexity: O(k*log(n))
    # Space complexity: O(n)


def findKthLargest3(nums, k):
    def select(list, l, r, index):
        if l == r:
            return list[l]
        import random 
        pivot_index = random.randint(l, r)
        # move pivot to the beginning of list
        list[l], list[pivot_index] = list[pivot_index], list[l]
        # partition
        i = l
        for j in range(l + 1, r + 1):
            if list[j] < list[l]:
                i += 1
                list[i], list[j] = list[j], list[i]
        # move pivot to the correct location
        list[i], list[l] = list[l], list[i]
        # recursively partition one side
        if index == i:
            return list[i]
        elif index < i:
            return select(list, l, i - 1, index)
        else:
            return select(list, i + 1, r, index)
    
    return select(nums, 0, len(nums) - 1, len(nums) - k)

print('[3,2,3,1,2,4,5,5,6] and k = 4')
print( findKthLargest3([3,2,3,1,2,4,5,5,6],4) )
print('')
print('[3,2,1,5,6,4] and k=2')
print( findKthLargest3([3,2,1,5,6,4],2) )