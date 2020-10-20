def paths_through_maze(maze):
    paths = [ [0] * len(maze[0]) for _ in range(len(maze))]
    paths[0][0] = 1
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if val == 1 or (i == 0 and j == 0):
                continue
            
            leftPaths = 0
            topPaths = 0
            if i > 0:
                leftPaths = paths[i-1][j]
            if j > 0:
                topPaths = paths[i][j-1]
            paths[i][j] = leftPaths + topPaths
        print(paths)
        return paths[-1][-1]
    
print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))  