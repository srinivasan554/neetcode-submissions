class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mp = dict()
        
        for i, num in enumerate(nums):
            new_target = target - num

            if(new_target in mp):
                return [mp[new_target],i]
            
            mp[num] = i

        return []