'''
给一个整数数组 nums ，判断是否存在三元组
[nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k 
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
'''


class Solution:
    def threeSum(self, nums):
        nums.sort()  # 先对数组进行排序，方便后续操作
        result = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复的数字，避免重复结果
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复的数字，避免重复结果
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # 当前和小于 0，增大较小数
                else:
                    right -= 1  # 当前和大于 0，减小较大数
        return result
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))