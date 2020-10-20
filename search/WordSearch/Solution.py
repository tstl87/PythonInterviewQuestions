class Solution:
	def exist(self, board, word):
		visited = {}

		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.getWords(board, word, i, j, visited):
					return True
		
		return False

	def getWords(self, board, word, i, j, visited, pos = 0):
		if pos == len(word):
			return True

		if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
			return False

		visited[(i, j)] = True
		res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
				or self.getWords(board, word, i, j - 1, visited, pos + 1) \
				or self.getWords(board, word, i + 1, j, visited, pos + 1) \
				or self.getWords(board, word, i - 1, j, visited, pos + 1)
		visited[(i, j)] = False

		return res
		
print( Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED"))

class Grid(object):
  def __init__(self, matrix):
    self.matrix = matrix

  def __wordSearchRight(self, index, word):
    for i in range(len(self.matrix[index])):
      if word[i] != self.matrix[index][i]:
        return False
    return True

  def __wordSearchBottom(self, index, word):
    for i in range(len(self.matrix)):
      if word[i] != self.matrix[i][index]:
        return False
    return True

  def wordSearch(self, word):
    for i in range(len(self.matrix)):
      if self.__wordSearchRight(i, word):
        return True
    for i in range(len(self.matrix[0])):
      if self.__wordSearchBottom(i, word):
        return True
    return False

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

print(Grid(matrix).wordSearch('FOAM'))
# True