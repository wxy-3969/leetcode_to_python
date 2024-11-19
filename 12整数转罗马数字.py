'''
七个不同的符号代表罗马数字，其值如下：
符号值
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：
如果该值不是以4或9开头,请选择可以从输入中减去的最大值的符号，将该符号附加到结果,减去其值,然后将其余部分转换为罗马数字。
如果该值以4或9开头,使用减法形式,表示从以下符号中减去一个符号
例如4是5(V)减1(I):IV,9是10(X)减1(I):IX。
仅使用以下减法形式:4 (IV),9 (IX),40 (XL),90(XC),400(CD)和900(CM)。
只有10的次方（I, X, C, M）最多可以连续附加3次以代表10的倍数。
你不能多次附加5(V)，50(L)或500(D)如果需要将符号附加4次,请使用 减法形式。
给定一个整数,将其转换为罗马数字。
'''

class Solution:
    def intToRoman(self, num):
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        roman_num = ""
        for value, symbol in roman_numerals:    # 遍历罗马数字列
            count = num // value
            roman_num += symbol * count    # 拼接对应的符号
            num %= value
        return roman_num
# 测试
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(20))
