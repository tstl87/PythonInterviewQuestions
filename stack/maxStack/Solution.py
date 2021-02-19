class MaxStack:
  def __init__(self):
    self.stack = []
    self.maxes = []

  def push(self, value):

    self.stack.append(value)
    if not self.maxes or value > self.maxes[-1]:
      self.maxes.append(value)
    else:
      self.maxes.append(self.maxes[-1]) 

  def pop(self):
    self.maxes.pop()
    return self.stack.pop()

  def max(self):
    return self.maxes[-1]

stack = MaxStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(2)

print( 'max ', stack.max())
print( stack.pop())
print( 'max ', stack.max())
print( stack.pop())
print( 'max ', stack.max())
print( stack.pop())
print( 'max ', stack.max())
print( stack.pop())


