class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic={}
        dic1={}

        for i in ransomNote:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for i in magazine:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i]=1
        
        for i, count in dic.items():
            if i not in dic1:
                return False 

            if dic1[i] < count:
                return False
        return True
                