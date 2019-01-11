import math

#1.两数之和
def twoSum(nums, target):

    num_dict = {}

    for i in range(len(nums)):
        num_dict[nums[i]] = i

    for i in range(len(nums)):
        num = target - nums[i]
        if num in num_dict and num_dict[num] != i:
            return [i, num_dict[target - nums[i]]]

    return []

#2.有效的数独
def isValidSudoku(board):
    for i in range(9):
        col_dict = {}
        row_dict = {}
        sqr_dict = {}
        for j in range(9):

            c = board[i][j]
            if c == '.':
                c = '.'
            elif int(c) in row_dict:
                return False
            else:
                row_dict[int(c)] = 0

            c = board[j][i]
            if c == '.':
                c = '.'
            elif int(c) in col_dict:
                return False
            else:
                col_dict[int(c)] = 0

            c = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
            if c == '.':
                c = '.'
            elif int(c) in sqr_dict:
                return False
            else:
                sqr_dict[int(c)] = 0
    return True

#3.字母异位分组
def groupAnagrams(strs):
    d = {}
    result = []

    for s in strs:
        l = list(s)
        l.sort()
        l = ''.join(l)
        if l not in d:
            d[l] = []
        d[l].append(s)

    for key in d.keys():
        result.append(d[key])
    return result

#4.最小覆盖子串
def minWindow(s, t):
    s_len = len(s)
    t_len = len(t)

    if s_len == 0 or t_len == 0:
        return ''

    d_s = {}
    d_t = {}

    for i in t:
        if i not in d_t:
            d_t[i] = 0
        d_t[i] += 1

    min_len = s_len
    begin = -1
    start = 0
    found = 0

    for i in range(len(s)):
        #将字符串s中的字符放入哈希中
        if s[i] not in d_s:
            d_s[s[i]] = 0
        d_s[s[i]] += 1

        #如果当前字符串在字符串t中，并且其数量小于等于在字符串t中的数量，表示匹配到了一个字符
        if s[i] in d_t and d_s[s[i]] <= d_t[s[i]]:
            found += 1

        #当匹配字符的个数等于t的长度时，表示匹配到一个包含t所有字符的子串
        if found == t_len:
            #从当前包含t所有字符的子串中删除开头没用的字符，两种情况
            #1.首字母不在t中
            #2.首字母在t中，但是出现次数大于t中出现次数
            while start < i  and (s[start] not in d_t or d_s[s[start]] > d_t[s[start]]):
                d_s[s[start]] -= 1
                start += 1

            #如果删除完开头的子字符串比前一个字符串短，说明匹配到新的字符串
            if i - start < min_len:
                min_len = i - start
                begin = start

            #为了查找下一个子字符串，将当前匹配到所有字符的子串的首位加一，继续查找
            d_s[s[start]] -= 1
            start += 1
            found -= 1

    if begin == -1:
        return ''
    else:
        return s[begin : begin + min_len + 1]

#5.直线上最多的点数
def maxPoints(points):
    if len(points) == 0:
        return 0
    if len(points) == 1:
        return 1

    result = 0

    for i in range(len(points)):
        same_point = 0
        d_lines = {}
        for j in range(i + 1, len(points)):
            x_1, y_1 = points[i]
            x_2, y_2 = points[j]

            if x_1 == x_2 and y_1 == y_2:
                same_point += 1
            elif x_1 == x_2:
                if 'x=' + str(x_1) not in d_lines:
                    d_lines['x=' + str(x_1)] = 0
                d_lines['x=' + str(x_1)] += 1
            elif y_1 == y_2:
                if 'y=' + str(y_1) not in d_lines:
                    d_lines['y=' + str(y_1)] = 0
                d_lines['y=' + str(y_1)] += 1
            else:
                dx = x_2 - x_1
                dy = y_2 - y_1

                if (dx < 0 and dy < 0) or (dx > 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                a = abs(dx) if abs(dx) < abs(dy) else abs(dy)
                b = abs(dx) if abs(dx) >= abs(dy) else abs(dy)
                while a > 0:
                    rem = b % a
                    b = a
                    a = rem
                if b != 0:
                    dx /= b
                    dy /= b
                if str(dy) + '/' + str(dx) not in d_lines:
                    d_lines[str(dy) + '/' + str(dx)] = 0
                d_lines[str(dy) + '/' + str(dx)] += 1
        max_points = 0
        print(d_lines)
        for key in d_lines.keys():
            if d_lines[key] > max_points:
                max_points = d_lines[key]
        max_points +=  same_point + 1
        if max_points > result:
            result = max_points
    return result

print(maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))
print(maxPoints([[1,1],[2,2],[3,3]]))
print(maxPoints([[3,10],[0,2],[0,2],[3,10]]))
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))