class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = set()

        l, r = 0,0

        n = len(s)

        res = 0

        while(r < n):
            if(s[r] not in mp):
                mp.add(s[r])
                res = max(res , r -l + 1)

            else:
                while(s[r] in mp):
                    mp.remove(s[l])
                    l += 1
                mp.add(s[r])
            r += 1

        return res