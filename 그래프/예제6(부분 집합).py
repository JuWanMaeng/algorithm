"""
모든 부분 집합을 리턴하라

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

class Solution:
    def subsets(self, nums):
        result=[]

        def dfs(index,path):
            result.append(path)

            for i in range(index,len(nums)):
                dfs(i+1,path+[nums[i]])

        dfs(0,[])
        return result

test=Solution()
print(test.subsets([1,2,3]))
        