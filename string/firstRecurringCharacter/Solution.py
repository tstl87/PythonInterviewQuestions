def first_char(s):
    seen = set()
    
    for ch in s:
        if ch in seen:
            return ch
        else:
            seen.add(ch)
            
    return False

print( first_char('qwertty'))

print( first_char('qwerty'))


