class Solution(object):
    def pivotIndex(self, nums):
        lsum = 0
        total = 0
        for num in nums:
            total += num

        for i in range(len(nums)):
            right = total - lsum - nums[i]
            if lsum == right:
                return i
            lsum += nums[i]
        return -1