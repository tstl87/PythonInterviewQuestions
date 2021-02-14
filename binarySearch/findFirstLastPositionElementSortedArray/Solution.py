class Solution:
  def getRange(self, arr, target):

    #first = self.binarySearch(arr, target, 0, len(arr)-1, True)
    #last = self.binarySearch(arr, target, 0, len(arr)-1, False)

    first = self.binarySearchIterative(arr, target, 0, len(arr)-1, True)
    last = self.binarySearchIterative(arr, target, 0, len(arr)-1, False)

    return [first, last]

  def binarySearch(self, arr, target, low, high, findFirst):
    if high < low:
      return -1
    
    # update mid point using
    # better version of (high + low ) / 2
    mid = low + (high - low) // 2
    
    # find first occurrence of target in the array
    if findFirst:
      # if mid becomes one of the end points of the array.
      if mid == 0 or mid == len(arr) -1:
        return mid
      
      # if first occurence is found
      if arr[mid] == target:
        if arr[mid -1] < target:
          return mid
        else:
          return self.binarySearch(arr, target, low, mid-1, True)
      # arr[mid] < target, search again in [mid+1, high] 
      elif arr[mid] < target:
        return self.binarySearch(arr, target, mid+1, high, True)
      # arr[mid] > target, search again in [low, mid-1]
      elif arr[mid] > target:
        return self.binarySearch(arr, target, low, mid-1, True)
    
    # find the last occurence of target in the array
    else:
      # if mid becomes one of the end points of the array.
      if mid == 0 or mid == len(arr) -1:
        return mid
      
      # if last occurence is found
      if arr[mid] == target:
        if arr[mid+1] > target:
          return mid
        else:
          return self.binarySearch(arr, target, mid+1, high, False)
      elif arr[mid] < target:
        return self.binarySearch(arr, target, mid+1, high, False)
      elif arr[mid] > target:
        return self.binarySearch(arr, target, low, mid-1, False)

  def binarySearchIterative(self, arr, target, low, high, findFirst):
    while True:
      # stop if high becomes less than low
      if high < low:
        return -1
      
      mid = low + (high - low) // 2
      # stop if mid becomes an endpoint
      if findFirst:
        if mid == 0 or mid == len(arr)-1:
          return mid
        if arr[mid] == target:
          if arr[mid-1] < target:
            return mid
          else:
            high = mid-1
        elif arr[mid] < target:
          low = mid+1
        elif arr[mid] > target:
          high = mid-1

      else:
        if mid == 0 or mid == len(arr)-1:
          return mid
        if arr[mid] == target:
          if arr[mid+1] > target:
            return mid
          else:
            low = mid+1
        elif arr[mid] < target:
          low = mid+1
        elif arr[mid] > target:
          high = mid-1
    



arr = [0, 1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
print(Solution().getRange(arr, 9))
# [7, 9]

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