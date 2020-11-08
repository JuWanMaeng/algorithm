import collections

class Solution:
    def groupAnagrams(self, strs):
        d=collections.defaultdict(list)
        for words in strs:
            d[''.join(sorted(words))].append(words)           #sorted 함수는 문자열도 리스트로 반환한다 ex) 'bca'->['a','b','c']  -->join 함수로 다시 'abc' 로 바꾸기 가능
        
        return d.values()

        
strs = ["eat","tea","tan","ate","nat","bat"]
test=Solution()
print(test.groupAnagrams(strs))

        