'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()    
        first = strs[0]
        last = strs[-1]
        prefix = ""    # 初始化公共前缀为空
        for i in range(min(len(first), len(last))):    # 比较第一个和最后一个字符串，取最短的长度
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        return prefix
#  测试
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))       