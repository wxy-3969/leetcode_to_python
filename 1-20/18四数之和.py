'''
给定一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] 
（若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
'''


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue  # 跳过重复数字
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue  # 跳过重复数字
                left = b + 1
                right = n - 1
                while left < right:
                    total = nums[a] + nums[b] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[a], nums[b], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # 跳过重复数字
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1  # 跳过重复数字
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))