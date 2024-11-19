'''
给定两个大小分别为m和n的正序(从小到大)数组nums1和nums2请你找出并返回这两个正序数组的中位数 。
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        # 二分查找
        low, high = 0, m
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            # 确定左边和右边的最大值和最小值
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            # 如果满足条件，则返回中位数
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            # 否则，移动指针
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1
# 测试
if __name__ == '__main__':
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2]
    obj = Solution()
    print(obj.findMedianSortedArrays(nums1, nums2))