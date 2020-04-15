class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],i]
            dic[num]=i
        return "Bummer"
    
ex_nums = [2, 7, 11, 15] 
ex_target = 9

print(Solution().twoSum(ex_nums,ex_target))