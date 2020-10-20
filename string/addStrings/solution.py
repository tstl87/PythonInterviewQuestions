class Solution:
    def addStrings1(self, num1: str, num2: str) -> str:
        
        rv = []
        carry = 0
        p1 = len(num1) -1
        p2 = len(num2) -1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            rv.append(value)
            p1 -= 1
            p2 -= 1
            
        if carry:
            res.append(carry)
            
        return ''.join(str(x) for x in rv[::-1])

    def merge(self, nums1, m, nums2, n):
 
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]
        