class Solution:
    def twoSum(self, nums, target):
        d=dict()
        for i, num in enumerate(nums):
            d[num]=i
        for i,num in enumerate(nums): #in 함수의 시간복잡도는 O(N)이지만 일일히 비교하는 것보다 파이썬에서는 더 빠르다
            if target-num in d and i!=d[target-num]:
                return nums.index(num), d[target-num]
test=Solution()
print(test.twoSum([2,7,11,15],9))




        