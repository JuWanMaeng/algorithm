""" 
많이 등장하는 것중 k번째 까지 return 해라

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

"""
import collections
import heapq

class Solution:
    def way1(self, nums, k):
        freqs=collections.Counter(nums)
        freqs_heap=[]

        for f in freqs:
            heapq.heappush(freqs_heap,(-freqs[f],f))

        topk=list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

    def way2(self,nums,k):        #zip 함수와 unpacking 사용
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


test=Solution()
print(test.way2([1,2],2))

        