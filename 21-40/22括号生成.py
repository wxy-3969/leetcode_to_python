'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''


class Solution:
    def generateParenthesis(self, n):
        result = []
        self.backtrack(result, "", 0, 0, n)
        return result
    def backtrack(self, result, current, open_count, close_count, n):    # 回溯算法
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:    # 如果左括号的数量小于n，则可以添加左括号
            self.backtrack(result, current + "(", open_count + 1, close_count, n)
        if close_count <open_count:    # 如果右括号的数量小于左括号的数量，则可以添加右括号
            self.backtrack(result, current + ")", open_count, close_count + 1, n)
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))