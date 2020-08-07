class Solution2:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res=[]
        self.DFS(candidates,target,0,res,[])
        return res
 
    def DFS(self,candidates,target,start,res,intermedia):
        if target==0:
            res.append(intermedia)
            return
        for i in range(start,len(candidates)):
            if target<candidates[i]:
                return
            self.DFS(candidates,target-candidates[i],i,res,intermedia+[candidates[i]])
 
val=Solution2()
n,tar=map(int,input().split())
can=list(map(int,input().split()))
print(*val.combinationSum(can,tar))
