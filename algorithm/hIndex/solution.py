def hIndex(pubs):
	n = len(pubs)
	freqs = [0] * (n + 1)

	# create a list of the count of papers
	# where the citation score is equal to the
	# list index score. If the score is greater
	# than the number of papers published, then
	# count it towards the end of the list.
	for pub in pubs:
		if pub >= n:
			freqs[n] += 1
		# otherwise
		else:
			freqs[pub] += 1

	
	# Run a backwards cumulative sum on the frequency list.
	# 
	total = 0
	i = n
	while i >= 0:
		total += freqs[i]
		if total >= i:
			return i
		i -= 1
	return 0


print(hIndex([5, 3, 3, 1, 0]))
# 3