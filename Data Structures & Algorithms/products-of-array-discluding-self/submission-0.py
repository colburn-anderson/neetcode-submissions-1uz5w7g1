class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * (len(nums))
        left = 1
        curr = 1

        for i in range(len(nums)):
            res[i] = curr
            curr *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= left
            left *= nums[i]

        return res        




        