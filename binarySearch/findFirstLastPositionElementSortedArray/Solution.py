class Solution:
    def getRange(self, arr, target):
        first = self.binarySearchIterative(arr,0,len(arr)-1, target, True)
        last = self.binarySearchIterative(arr,0,len(arr)-1, target, False)
        return [first, last]
    
    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            return -1
        mid = low + (high - low)//2
        if findFirst:
            if (mid == 0 or target > arr[mid-1]) and arr[mid] == arr[mid] == target:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr,mid+1,high,target,findFirst)
            else:
                return self.binarySearch(arr,low,mid-1,target,findFirst)
        else:
            if (mid == len(arr)-1 or target < arr[mid+1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]:
                return self.binarySearch(arr, low, mid-1, target, findFirst)
            else:
                return self.binarySearch(arr, mid+1, high, target, findFirst)
        
    def binarySearchIterative(self, arr, low, high, target, findFirst):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if findFirst:
                if (mid == 0 or target > arr[mid-1]) and arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if (mid== len(arr)-1 or target < arr[mid+1]) and arr[mid] == target:
                    return mid
                if target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
        
arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
x = 9
print(Solution().getRange(arr, 9))
# [6, 8]

# Iterative Solution:
# Time Complexity:
# Binary search algorithm on an ordered list of length n
# has a time complexity of O(log_2(n))

# Space Complexity:
# We are only creating and updating two variables so
# our space complexity is O(1)

# Recursive Soluition:
# Time Complexity:
# Binary search algorithm on an ordered list of length n
# has a time complexity of O(log_2(n))

# Space Complexity:
# Since we are using recursion, there is a Recusion cost
# that matches our time complexity cost of O(log_2(n)).