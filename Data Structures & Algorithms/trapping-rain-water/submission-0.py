class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        res = 0

        if n==0 or n==1:
            return res

        left_max_height = [0] * n
        right_max_height = [0] * n

        for i in range(1,n):
            left_max_height[i] = max(left_max_height[i-1],height[i-1])

        for j in range(n-2,0,-1):
            right_max_height[j] = max(right_max_height[j+1],height[j+1])

        for i in range(n):

            sol = min(left_max_height[i],right_max_height[i]) - height[i]

            if sol >=0:
                res += sol

        return res
