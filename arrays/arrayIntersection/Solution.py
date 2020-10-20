class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list( set1.intersection(set2))
    
    def intersection2(self, nums1, nums2):
        
        results = {}
        for num in nums1:
            if num in nums2 and num not in results:
                results[num] = 1
                
        return list(results.keys())
    
    def intersection3(self, nums1, nums2):
        
        hashh = {}
        duplicates = {}
        for i in nums1:
            hashh[i] = 1
        for i in nums2:
            if i in hash:
                duplicates[i] = 1
                
        return list(duplicates.keys())
    
    
print(Solution().intersection2([4, 9, 5], [9, 4, 9, 8, 4]))