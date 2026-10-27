class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            realT = target - n
            if realT in hashmap:
                return [hashmap[realT], i]
            hashmap[n] = i