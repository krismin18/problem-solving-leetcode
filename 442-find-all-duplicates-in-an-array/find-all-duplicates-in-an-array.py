class Solution(object):
    def findDuplicates(self, nums):
        dup = []
        for num in nums:
            
            ind = abs(num)-1
            if nums[ind] < 0:
                dup.append(abs(num))
            else:
                nums[ind] = -nums[ind]
        return dup
