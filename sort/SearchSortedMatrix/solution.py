def searchMatrix(mat, value):
    if len(mat) == 0:
        return False
    
    rows = len(mat)
    cols = len(mat[0])
    
    low = 0
    high = rows * cols
    while low < high:
        mid = (low + high) // 2
        mid_value = mat[mid // cols][mid % cols]
        
        if mid_value == value:
            return True
        if mid_value < value:
            low = mid + 1
        else:
            high = mid
            
    return False

mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True