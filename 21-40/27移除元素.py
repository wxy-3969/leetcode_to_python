'''
给你一个数组nums和一个值val,你需要原地移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回nums中与val不同的元素的数量。

假设nums中不等于 val 的元素数量为 k,要通过此题，您需要执行以下操作：
更改nums数组,使nums的前k个元素包含不等于val的元素。nums的其余元素和nums的大小并不重要。
返回 k。
'''


class Solution:
    def removeElement(self, nums, val):
        if not nums:    # 如果nums为空，直接返回0
            return 0
        new_index = 0
        for num in nums:    # 遍历nums中的每个元素
            if num!= val:
                nums[new_index] = num    # 将不等于val的元素放到新数组中    
                new_index += 1
        return new_index
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([3,2,2,3], 3))