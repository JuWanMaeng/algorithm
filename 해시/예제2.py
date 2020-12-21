"""
중복 문자 없는 가장 긴 부분 문자열의 길이를 리턴하라
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: s = ""
Output: 0 
"""
import collections

class Solution:
    def way(self,s:str):
        used={}
        max_length=start=0
        for index,char in enumerate(s):
            if char in used and start <=used[char]:
                start=used[char]+1
            else:
                max_length=max(max_length,index-start+1)
            
            used[char]=index

        return max_length

test=Solution()
print(test.way('pwwkew'))


