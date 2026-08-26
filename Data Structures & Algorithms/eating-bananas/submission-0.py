class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        res= r
        
        
        while (l <= r):
            expected_hr_eating = 0

            rate_of_eating = l + (r-l)//2

            for pile in piles:
                expected_hr_eating += (pile + rate_of_eating - 1)//rate_of_eating

                if(expected_hr_eating > h): break

            if(expected_hr_eating <= h):
                res = rate_of_eating
                r = rate_of_eating - 1
            
            else:
                
                l = rate_of_eating + 1

        return res

