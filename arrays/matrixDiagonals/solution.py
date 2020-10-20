m = [[0, 1, 2],
	 [3, 4, 5],
	 [6, 7, 8],
	 [9, 0, 1]]


class solution:
	def printDiag(self, m):

		M = len(m)
		N = len(m[0])

		i = 0
		j = 0
		# Note that there are M + N - 1 diagonals
		for _ in range(M + N - 1):

			while( j <= N-1):
				self.printDiag_helper(m,i,j)
				j += 1
				if j == N:
					i += 1
					j -= 1
					break

			while( i <= M-1):
				self.printDiag_helper(m,i,j)
				i += 1

	def printDiag_helper(self, m,i,j):
		M = len(m)

		output = '' 
		while ( j >= 0 and i <= M-1 ):
			output += str(m[i][j]) + ' '
			j -= 1
			i += 1

		print(output)

print(solution().printDiag(m))

