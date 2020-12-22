"""
2 에서 9 까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력하라.

입력:23
출력:["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

"""
class Solution:
    def letterCombinations(self, digits: str):
        result=[]

        def dfs(index,path):
            if(len(digits)==len(path)):
                result.append(path)
                return

            for i in range(index,len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)

        if not digits:
            return []

        dfs(0,"")


        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        return result
    
    
