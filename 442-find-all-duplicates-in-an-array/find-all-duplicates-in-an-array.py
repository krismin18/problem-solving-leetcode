class Solution(object):
    def findDuplicates(self, nums):
        dup = []
        
        ctr = Counter(nums)
        for i, j in ctr.items():
            if j > 1:
                dup.append(i)

        return dup
