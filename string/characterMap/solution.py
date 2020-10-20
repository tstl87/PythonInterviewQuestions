def has_character_map(s1,s2):
    if len(s1) != len(s2):
        return False
    
    chars = {}
    for i in range(len(s1)):
        if s1[i] not in chars:
            chars[s1[i]] = s2[i]
        else:
            if chars[s1[i]] != s2[i]:
                return False
    return True

print(has_character_map('abc','def'))
# True

print(has_character_map('aac','def'))
# False