class Solution:
    def combinationSum(self, candidates, target):
        result=[]

        def dfs(csum,index,path):
            if csum<0:
                return
            if csum==0:
                result.append(path)
                return

            for i in range(index,len(candidates)):                  #매우 중요한 부분 함수로 보내면서 원소를 추가했다
                dfs(csum-candidates[i],i,path+[candidates[i]])    
        
        dfs(target,0,[])
        return result

test=Solution()
print(test.combinationSum([2,3,6,7],7))