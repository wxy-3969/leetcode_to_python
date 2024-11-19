'''
罗马数字包含以下七种字符: I,V,X,L,C,D和M
字符    数值
I        1
V        5
X        10
L        50
C        100
D        500
M        1000
例如:罗马数字2写做II,即为两个并列的。12写做XII即为 X+II。27写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII,
而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况:
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。
'''


class Solution:
    def romanToInt(self, s):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:# 如果当前字符的值小于下一个字符的值，则减去当前字符的值  
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        return result
# 测试
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))