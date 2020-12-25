import itertools
class Solution:
    def combine(self, n: int, k: int):
        result=[]

        def dfs(elements, start, k):
            if k==0:
                result.append(elements[:])

            for i in range(start,n+1):
                elements.append(i)
                dfs(elements,i+1,k-1)
                elements.pop()

        dfs([],1,k)
        return result   

    def way2(self,n,k):
        return list(map(list,itertools.combinations(range(1,n+1),k)))

test=Solution()
print(test.combine(4,2))
print(test.way2(4,2))