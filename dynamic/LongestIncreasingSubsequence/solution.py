def longest_increasing_subsequence(arr):
  cache = [1] * len(arr)
  for i in range(1, len(arr)):
    for j in range(i):
      if arr[i] > arr[j]:
        cache[i] = max(cache[i], cache[j] + 1)
  return max(cache)


print(longest_increasing_subsequence(
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]))
# 5