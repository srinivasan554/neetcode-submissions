class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mp = set()

        res = 0

        for num in nums:
            mp.add(num)
            res = 1

        for num in nums:
            #if previous is not there
            if((num - 1) not in mp):
                count = 1
                next_num = num + 1
                # go on till you have no next num in the set
                while((next_num) in mp):
                    count += 1
                    next_num += 1
                res = max(count, res)
            else:
                continue
        return res