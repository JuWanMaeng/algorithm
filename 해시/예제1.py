# J는 보석ㅇ이며 S는 갖고있는 돌이다. S에는 보석이 몇개나 있을까? 대소문자는 구분한다
# J = "aA" S="aAAbbbb"  출력:3

import collections

class Solution:
    def way1(self, J: str, S: str):          #defaultdict 이용
        freqs=collections.defaultdict(int)
        count=0

        for char in S:
            freqs[char]+=1
        
        for char in J:
            count+=freqs[char]

        return count

    def way2(self,J,S):                     #Counter 로 계산 생략
        freqs=collections.Counter(S)
        count=0

        for char in J:
            count+=freqs[char]

        return count

    def way3(self,J,S):
        return sum(s in J for s in S)

        # [s for s in S] --> ['a','A','A','b','b','b','b']
        # [s in J for s in S] --> [True,True,True,False,F,F,F]