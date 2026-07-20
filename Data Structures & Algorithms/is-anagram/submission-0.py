class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if (m != n):
            return False

        else:
            mp = dict()
            mp1 = dict()

            for c in s:
                if(c not in mp):
                    mp[c] = 1
                else:
                    mp[c] = mp[c] + 1
            
            for c in t:
                if(c not in mp1):
                    mp1[c] = 1
                else:
                    mp1[c] = mp1[c] + 1

        for key,val in mp.items():
            if(val != mp1.get(key,0)):
                return False

        return True