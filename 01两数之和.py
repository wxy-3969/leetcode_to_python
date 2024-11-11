'''
给定一个整数数组 nums 和一个整数目标值 target,请你在该数组中找出和为目标值target的那两个整数,并返回它们的数组下标.
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
'''
class Solution:
    def twoSum(self, nums, target):
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return [] 
# 测试用例
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
