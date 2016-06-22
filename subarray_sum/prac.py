class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        index = sorted(range(len(nums)), key=lambda x: nums[x])
        l, r = 0, len(index)-1
        while l < r:
            local_sum = nums[index[l]] + nums[index[r]]
            if local_sum == 0:
                return sorted([index[l], index[r]])
            elif local_sum > 0:
                r -= 1
            else:
                l += 1
        return sorted([index[l], index[r]])

if __name__ == "__main__":
    sl = Solution()
    nums = [-3,1,2,-3,4]
    print sl.subarraySum(nums)