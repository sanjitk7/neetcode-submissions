class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        u = rows * cols - 1
        while l <= u:
            m = (l + u)//2
            row = m // cols
            col = m % cols
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                u = m - 1
            else:
                return True
        return False
