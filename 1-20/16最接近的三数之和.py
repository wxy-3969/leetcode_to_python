'''
给定一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
'''


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # 对数组进行排序
        n = len(nums)
        closest_sum = float('inf')  # 初始化最接近的和为正无穷
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:  # 如果找到等于目标值的和，直接返回
                    return total
                if abs(total - target) < abs(closest_sum - target):  # 更新最接近的和
                    closest_sum = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))