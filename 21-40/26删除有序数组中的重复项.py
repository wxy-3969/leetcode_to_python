'''
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
'''


class Solution:
    def removeDuplicates(self, nums):
        if not nums:    # 如果数组为空，直接返回0
            return 0
        unique_index = 0
        for i in range(1, len(nums)):     # 遍历数组，如果当前元素与前一个元素不同，则将其放到数组的第一个不同的元素的位置上
            if nums[i]!= nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        return unique_index + 1
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 2]))