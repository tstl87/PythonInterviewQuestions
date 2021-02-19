class Solution:
  def pushDominoes(self, dominoes):
    maxForce = len(dominoes)
    forces = [0]*maxForce

    # Apply right dominoe force
    force = 0
    for i, d in enumerate(dominoes):
      if d == 'R':
          force = maxForce 
      elif d == 'L':
          force = 0
      else:
        force = max(0, force - 1)
      forces[i] += force

    # Apply left dominoe force
    force = 0
    for i in range( maxForce-1, -1, -1):
      if dominoes[i] == 'R':
        force = 0 
      elif dominoes[i] == 'L':
        force = maxForce
      else:
        force = max(0, force -1)
      forces[i] -= force

    
    ret = ''
    for i in range(maxForce):
      if forces[i] > 0:
        ret += 'R'
      elif forces[i] < 0:
        ret += 'L'
      else:
        ret += '.'

    return ret

print(Solution().pushDominoes('.R...L..R.'))
# .RR.LL..RR