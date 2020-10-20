def findTime(tasks, cooldown):
    lastPos = {}
    current = 0
    
    for task in tasks:
        if task in lastPos:
            if current - lastPos[task] <= cooldown:
                #add cooldown
                current = cooldown + lastPos[task] + 1
        lastPos[task] = current
        current += 1
        
    return current

print(findTime([1,1,2,1],2))