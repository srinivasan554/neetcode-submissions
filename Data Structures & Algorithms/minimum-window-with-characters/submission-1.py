class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return t

        m,n = len(s), len(t)

        countT = {}

        # get the t frequency

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)

        window = {}

        res = float('infinity')

        l, r = 0,0

        sol = [-1,-1]

        for c in s:
            #create window
            window[c] = window.get(c,0) + 1
            r += 1
            if (c in countT and countT[c] == window[c]):
                have += 1
            
            while (have == need):
                if(res > (r -l + 1)):
                    sol = [l,r]
                res = min(res, r - l + 1)

                # shrink the window

                window[s[l]] = window.get(s[l],0) - 1
                

                if(s[l] in countT and window[s[l]] < countT[s[l]]):
                    have -= 1
                    l += 1
                    break

                l += 1
                
        i1, i2 = sol

        return s[i1:i2] if i1 != -1 else ""

