'''
给定一个长度为n的整数数组height,有n条垂线,第i条线的两个端点是(i, 0)和(i,height[i])。
找出其中的两条线,使得它们与x轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
'''


class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1  # 初始化双指针，分别指向数组的首尾
        max_water = 0  # 用于记录最大盛水量
        while left < right:
            # 计算当前指针所指两条垂线构成容器的盛水量
            extent = min(height[left], height[right]) * (right - left)  
            max_water = max(max_water, extent)  # 更新最大盛水量
            if height[left] < height[right]:
                current_height = height[left]  # 记录当前较小的高度值
                left += 1
                while left < right and height[left] <= current_height:
                    # 当左指针右移,若新位置高度不大于之前记录的较小高度，继续右移左指针
                    left += 1  
            else:
                current_height = height[right]
                right -= 1
                while left < right and height[right] <= current_height:
                    right -= 1
        return max_water
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.maximum_area([4, 8, 6, 2, 5, 4, 8, 3, 7]))

