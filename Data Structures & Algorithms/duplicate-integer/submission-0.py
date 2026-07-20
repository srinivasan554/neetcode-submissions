class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = set()
        for num in nums:
            if(num not in mp):
                mp.add(num)
            else:
                return True
        return False