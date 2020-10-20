def square_numbers(nums):

	# index to go backwards through the negative numbers
	neg_i = -1
	# index to go through the positive numbers.
	i = 0

	result = []
	for n in nums:
		if n >= 0:
			# update neg_i to be the location of the largest negative number.
			if neg_i == -1:
				neg_i = i - 1

			while neg_i >= 0 and nums[neg_i] < 0 and -nums[neg_i] < nums[i]:
				val = nums[neg_i]
				result.append(val * val)
				neg_i -= 1

			val = nums[i]
			result.append(val * val)
		i += 1

	while neg_i >= 0 and nums[neg_i] < 0:
		val = nums[neg_i]
		result.append(val * val)
		neg_i -= 1

	return result


#print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
#print(square_numbers([-9,-6,-5,-2,-1,0,3,4,7,8]))
print(square_numbers([-3,-2,-1,0,1,2,3]))

