import collections
from collections import defaultdict
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        
        words = re.sub("[!?',;.]", ' ', paragraph.lower()).split()  ##re 를 통한 치환
        d=defaultdict(int)
        for word in words:
            if word not in banned:
                d[word]+=1
        
        
        
        # count=collections.Counter(word)    제한 문자가 없다면 개수 세는데 용이할듯 
        
        
        return max(d,key=d.get)

test=Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
print(test.mostCommonWord(paragraph,['hit']))