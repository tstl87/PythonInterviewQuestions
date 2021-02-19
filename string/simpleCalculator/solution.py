class Solution(object):
  def eval(self, expression):
    return self._evalHelper(expression, 0)[0]
  
  def _evalHelper(self, expression, i):
    op = '+'
    result = 0
    while i < len(expression):
      char = expression[i]
      if char in set(['+', '-']):
        op = char
      else:
        value = 0
        if char.isdigit():
          value = int(char)
          if op == '+':
            result += value
          else:
            result -= value
        elif char == '(':
          (value, i) = self._evalHelper(expression, i+1)
          if op == '+':
            result += value
          else:
            result -= value
      i += 1
    return result, i

print(Solution().eval('(1 + (2 + (3 + (4 + 5))))'))
# 15