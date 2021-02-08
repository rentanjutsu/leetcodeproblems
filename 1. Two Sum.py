class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            value = target - i
            if value in nums:
                if value == i:
                    return nums.index(i), nums.index(value, (nums.index(i) + 1))
                else:
                    return nums.index(i), nums.index(value)
