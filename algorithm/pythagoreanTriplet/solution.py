class Solution:
  def containsPythagoreanTriplet1(self, nums):

    for a in nums:
      for b in nums:
        for c in nums:
          if a*a + b*b == c*c:
            return True 
  
    return False 

  def containsPythagoreanTriplet2(self, nums):

    squares = set(num*num for num in nums)

    for a in nums:
      for b in nums:
        if a*a + b*b in squares:
          return True

    return False

print( Solution().containsPythagoreanTriplet1( [3,4,1,2,5] ))

print( Solution().containsPythagoreanTriplet2([3,4,1,2,5]) )