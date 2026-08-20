class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix), len(matrix[0])

        #determine the row

        l, r = 0, m - 1

        while (l<=r):
            mid = l + ((r-l)//2)

            if(matrix[mid][0]==target):
                return True

            elif(matrix[mid][0] < target and matrix[mid][n-1] >= target):
                break

            elif(matrix[mid][0] < target and matrix[mid][n-1] < target):
                l = mid + 1
            else:
                r = mid - 1

        ## mid points to the current row

        tr = mid

        l, r = 0, n-1

        while (l<=r):

            mid = l + ((r-l)//2)

            if(matrix[tr][mid]==target):
                return True

            elif(matrix[tr][mid] < target):
                l = mid + 1
            else:
                r = mid - 1
                
        return False

        