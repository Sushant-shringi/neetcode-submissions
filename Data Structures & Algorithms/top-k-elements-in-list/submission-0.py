class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic={}

        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        
        ans=[]
        for i in range(k):
            ans.append(sorted_dict[i][0])
        return ans



            

