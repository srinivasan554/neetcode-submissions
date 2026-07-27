class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)

        m = len(s)
        n = len(t)

        if m!=n :
            return False
        
        for i in range (m):
            mp[s[i]] += 1
            mp[t[i]] -= 1

        for key,val in mp.items():
            if(val!=0):
                return False

        return True