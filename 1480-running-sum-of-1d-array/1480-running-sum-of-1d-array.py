class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        new_number = nums[0]
        res.append(new_number)
        #print(new_number)
        for i in range(1, len(nums)):
            new_number = new_number + nums[i]
            res.append(new_number)
        return res          
            