import collections

def hashkey(str):
    return "".join(sorted(str))

def hashkey2(str):
    arr = [0]*26
    for c in str:
        arr[ord(c) - ord('a')] = 1
    return tuple(arr)

def groupAnagramWords(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[hashkey2(s)].append(s)
    
    return tuple(groups.values())

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
