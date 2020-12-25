""" 
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""
import itertools


class Solution:
    def permute(self, nums):

        results=[]
        prev_elements=[]

        def dfs(elements):
            if len(elements)==0:                   #리프노드일때 결과 추가
                results.append(prev_elements[:])   # 파이썬은 모든 객체를 참조하는 형태로 처리되므로 만약 results.append(prev_elements)를 하게 되면 
                                                   # 결과값이 추가되는 게 아닌 prev_elements에 대한 참조가 추가되며, 이 경우 참조된 갑싱 변경될 경우 같이 바뀌게 된다
            for e in elements:                     #순열 생성 재귀호출
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        return results
    
    def way2(self,nums):                          #itertools 모듈 사용
        return list(map(list,itertools.permutations(nums,2)))

test=Solution()
print(test.way2([1,2,3]))


        