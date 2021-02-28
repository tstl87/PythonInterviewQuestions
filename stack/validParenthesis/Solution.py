
class Solution():
  def isValid(self, string):
    # stack to store and pop parenthesis
    stack = []
    leftPar = { '(':')', '[':']', '{':'}'}
    rightPar = { ')':'(', ']':'[', '}':'{'}

    for char in string:
      if char in leftPar:
          stack.append(char)
      elif char in rightPar:
        if len(stack) == 0 or stack[-1] != rightPar[char]:
          return False
        else:
          stack.pop()
      else:
        return False

    return len(stack) == 0


            
print( Solution().isValid('[](){}'))
# True
print( Solution().isValid("(]"))
# False
print( Solution().isValid("([)]"))
# False
print( Solution().isValid("{[]}"))
# True