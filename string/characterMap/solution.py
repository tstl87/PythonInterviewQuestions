def isomorphicCharacterMap1(s,t):
    
    if( len(s) != len(t)):
    	return False

    sDict, tDict = {}, {}

    # O(n) time and storage
    for i in range(len(s)):

    	if s[i] not in sDict:
    		sDict[s[i]] = 1
    	else:
    		sDict[s[i]] += 1

    	if t[i] not in tDict:
    		tDict[t[i]] = 1
    	else:
    		tDict[t[i]] += 1

    # O(n*log(n)) for the sort + O(n) for list conversion and O(n) memory storage for sVal and tVal)
    sVal, tVal = list(sDict.values()).sort(), list(tDict.values()).sort()

    if( sVal == tVal ):
    	return True
    else:
    	return False

def isomorphicCharacterMap2(s,t):

	if( len(s) != len(t)):
		return False

	from collections import Counter

	sCounter, tCounter = Counter(), Counter()
	
	for i in range(len(s)):
		if sCounter[s[i]] != tCounter[t[i]]: 
			return False
		sCounter[s[i]] = i+1
		tCounter[t[i]] = i+1

	return True



print(isomorphicCharacterMap2('abc','def'))
# True

print(isomorphicCharacterMap2('aabc','deff'))
# True

'''
isomorphicCharacterMap1
Let n = len(s) + len(t), then the run time for this method is O(n*log(n) + 2n) = O(n*log(n))
and the memory requirements is O(2n) = O(n)

time: O(n*log(n))
memory: O(n)

isomorphicCharacterMap2
'''