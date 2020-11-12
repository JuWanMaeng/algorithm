import collections

class Solution:
    def groupAnagrams(self, strs):
        d=collections.defaultdict(list)
        for words in strs:
            d[''.join(sorted(words))].append(words)           
        
        return d.values()

        
strs = ["eat","tea","tan","ate","nat","bat"]
test=Solution()
print(test.groupAnagrams(strs))

        