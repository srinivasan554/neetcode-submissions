class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs_mp = dict()
        for i,s in enumerate(strs):
            s_sort = "".join(sorted(s))
            if(s_sort not in sort_strs_mp):
                sort_strs_mp[s_sort] = []
            sort_strs_mp[s_sort].append(i)
            
        sol = []
        for key,vals in sort_strs_mp.items():
            

            temp = []

            for val in vals:
                temp.append(strs[val])
            
            sol.append(temp)
        

        return sol