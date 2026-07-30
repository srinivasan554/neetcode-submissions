class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m, n = len(s1), len(s2)

        if m > n : return False

        s1_freq = dict()

        s2_freq = dict()

        for i in range(m):
            s1_freq[s1[i]] = s1_freq.get(s1[i],0) + 1
            s2_freq[s2[i]] = s2_freq.get(s2[i],0) + 1

        r = m-1
        l = 0

        while (r < n):
            match = True
            for key,val in s1_freq.items():
                if(key not in s2_freq or val != s2_freq[key]):
                    match = False
                    break
            if match : return True

            s2_freq[s2[l]] -= 1

            l += 1
            r += 1

            if(r < n): 
                s2_freq[s2[r]] = s2_freq.get(s2[r],0) + 1
        
        return False
