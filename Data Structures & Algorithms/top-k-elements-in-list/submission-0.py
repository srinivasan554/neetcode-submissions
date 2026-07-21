class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the frequency of each element
        count_mp = dict()

        for num in nums:
            if(num not in count_mp):
                count_mp[num] = 1
            else:
                count_mp[num] += 1
        # initialized a 2d list for mapping frequency as index and its element
        buckets = [[] for _ in range (len(nums) + 1)] 

        for ele,freq in count_mp.items():
            buckets[freq].append(ele)

        result = []

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
            
            if(len(result) == k):
                 return result
        return []