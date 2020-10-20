from collections import defaultdict

class Node():
    def __init__(self, value, left=None, right = None):
        self.val = value
        self.left = left
        self.right = right
        
def _build_frequencies(root,counter):
    if root == None:
        return 0
    total = root.val + \
        _build_frequencies(root.left, counter) + \
        _build_frequencies(root.right, counter)
    counter[total] += 1
    print(total)
    return total
        
def most_freq_subtree_sum(root):
    counter = defaultdict(int)
    _build_frequencies(root, counter)
    most_common_sum = 0
    for k in list(counter):
        if counter[k] > counter[most_common_sum]:
            most_common_sum = k
    return most_common_sum

root = Node(3, Node(1), Node(-3))
print('answer = ', most_freq_subtree_sum(root))
# 1