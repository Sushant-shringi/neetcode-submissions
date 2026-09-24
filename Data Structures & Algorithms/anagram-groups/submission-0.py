class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic={}

        for ch in strs:
            so=sorted(ch)
            s = "".join(so) 
            if s in dic:
                dic[s].append(ch)
                
            else:
                dic[s]=[ch]

        return list(dic.values())