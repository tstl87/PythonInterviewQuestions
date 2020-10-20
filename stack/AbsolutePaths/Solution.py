def clean_path(path):
    folders = path.split('/')
    stack = []
    
    for folder in folders:
        if folder == '.':
            pass
        if folder == '..':
            stack.pop()
        else:
            stack.append(folder)
    return '/'.join(stack)

path = '/users/tech/docs/.././desk/../'
print(clean_path(path))