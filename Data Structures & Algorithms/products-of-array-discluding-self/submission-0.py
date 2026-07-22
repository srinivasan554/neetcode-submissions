class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref_mul_list = [1] * len(nums)

        suffix_mul_list = [1] * len(nums)

        sol = [1] * len(nums)

        for i in range(1,len(nums)):

            pref_mul_list[i] = (pref_mul_list[i-1] * nums[i-1])

        for i in range(len(nums)-2,-1,-1):

            suffix_mul_list[i] = (suffix_mul_list[i+1] * nums[i+1])

        for i in range(len(nums)):

            pref_mul_list[i] =  pref_mul_list[i] * suffix_mul_list[i]

        return pref_mul_list