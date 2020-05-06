class Solution:
    def topKFrequent(self, nums, k):
        from collections import defaultdict
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        heap = []
        from heapq import heappush, heappop
        
        for key, v in count.items():
            heappush(heap, (v, key))
            if len(heap) > k:
                heappop(heap)
        res = []
        while len(heap) > 0:
            res.append(heappop(heap)[1])
        return res
    
print( Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))


# Time complexity O(n*log(k))
# In the second loop, you are iterating over your hashmap (worst case O(n))
# and then you are poushing and popping from your heap O(log(k)) so overall it's
# O(n*log(k)).

# Space Complexity:
# O(n)
# hashmap O(n)
# heap O(k)
