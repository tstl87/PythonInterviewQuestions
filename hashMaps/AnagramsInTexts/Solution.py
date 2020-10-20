from collections import Counter

def find_anagrams(s, t):
    ns, nt = len(s), len(t)
    if len(t) > len(s):
        return []

    t_count = Counter(t)
    s_count = Counter(s[0:len(t)])

    result = []
    for i in range( nt, ns):

        s_count[s[i]] += 1
        if s_count[s[i-nt]] == 1:
            del s_count[s[i-nt]]
        else:
            s_count[s[i-nt]] -= 1

        if s_count == t_count:
            result.append(i-nt+1)

    return result


print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]