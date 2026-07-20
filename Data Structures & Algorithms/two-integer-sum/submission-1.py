class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()

        for i,num in enumerate(nums):
            mp[num] = i

        for i,num in enumerate(nums):
            n_target = target - num

            if(n_target in mp and i != mp.get(n_target)):
                x = min(i, mp.get(n_target))
                y = max(i, mp.get(n_target))
                return [x,y]
        return [x,y]
            
            