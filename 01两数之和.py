'''
给定一个整数数组 nums 和一个整数目标值 target,请你在该数组中找出和为目标值target的那两个整数,并返回它们的数组下标.
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
'''
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}    # 创建一个字典，用于存储每个元素及其对应的索引
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:    # 如果目标元素在字典中存在，则返回它们的索引
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
