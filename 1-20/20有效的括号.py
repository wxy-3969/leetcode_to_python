'''
给定一个只包括 '(',')','{','}','[',']' 的字符串s,判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
'''


class Solution:
    def isValid(self, s):
        stack = []  # 创建一个空栈，用于存储左括号
        brackets_map = {'(': ')', '{': '}', '[': ']'}  # 定义左括号与右括号的对应关系
        for char in s:
            if char in brackets_map:  # 如果是左括号，将其压入栈中
                stack.append(char)
            elif stack and brackets_map[stack.pop()] == char:  # 如果是右括号且与栈顶左括号匹配
                continue
            else:  # 如果遇到不匹配的右括号或其他字符，字符串无效
                return False

        return not stack  # 如果栈为空，说明所有括号都匹配，字符串有效；否则无效
# 测试
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()[]{}"))   