'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        '''
        数字和字母的对应关系
        '''
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6':'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def backtrack(index, combination):    # 回溯函数，index是当前处理的数字索引，combination是当前的组
            if index == len(digits):
                result.append(combination)
                return
            letters = phone_map[digits[index]]
            for letter in letters:
                backtrack(index + 1, combination + letter)
        backtrack(0, "")
        return result
# 测试
if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("23"))