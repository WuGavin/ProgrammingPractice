from functools import reduce
import random

max_int = 2 ** 31 - 1

#1. 整数反转
def reverse(x):
    result = 0
    sign = 1 if x > 0 else -1
    x *= sign

    while x > 0:
        result = result * 10 + x % 10
        x //= 10

    if (sign < 0 and result > max_int + 1) or (sign > 0 and result > max_int):
        return 0

    return result * sign

#2. 回文数
def isPalindrome(x):
    if x < 0:
        return False
    return reverse(x) == x

#3. 字符串转换数字
def myAtoi(str):
    str = str.strip()
    result = 0
    sign = 1

    for i in range(len(str)):
        if i == 0 and str[i] == '-':
            sign = -1
        elif i == 0 and str[i] == '+':
            sign = 1
        elif not (str[i] >= '0' and str[i] <= '9'):
            break
        else:
            result = result * 10 + int(str[i])

    if sign < 0 and result > max_int + 1:
        return -(max_int + 1)
    elif sign > 0 and result > max_int:
        return max_int
    else:
        return result * sign

#4. 第K个排列
def getPermutation(n, k):
    result = ''
    s = 1
    nums = []
    for i in range(n):
        s *= (i + 1)
        nums.append(i + 1)
    k -= 1
    while n > 1:
        s /= n
        result += str(nums[k // s])
        del nums[k // s]
        n -= 1
        k %= s
    result += str(nums[0])

    return result

#5. LRU缓存机制
class LRUCache(object):

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = dict()
        self.keys = []
        

    def get(self, key):

        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            return self.cache[key]

        return -1
        

    def put(self, key, value):

        if key in self.cache:
            self.cache[key] = value
            self.keys.remove(key)
            self.keys.insert(0, key)
        elif len(self.keys) < self.capacity:
            self.keys.insert(0, key)
            self.cache[key] = value
        else:
            old_key = self.keys.pop()
            self.cache[key] = value
            self.cache.pop(old_key)
            self.keys.insert(0, key)

#6. 数组中的第k个最大元素
def findKthLargest(nums, k):
    k = len(nums) - k

    if k < 0:
        return -1

    start = 0
    end = len(nums) - 1


    while True:
        left = start
        right = end
        root = nums[start]
        while left < right:
            while left < right and nums[right] >= root:
                righ -= 1
            while left < right and nums[left] <= root:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        if left == k:
            return root
        nums[left], nums[start] = root, nums[left]

        if left > k:
            end = left - 1
        else:
            start = left + 1

#7. 链表随机节点
class Solution(object):

    def __init__(self, head):

        self.head = head

    def getRandom(self):

        result = self.head.val

        temp = head.next
        count = 0
        while temp != None:

            count += 1

            t = random.randint(0, count)

            if t == 0:
                result = temp.val

            temp = temp.next

        return result

#8. 两个有序数组间相加和的top k
def twoArraysAddup(a, b, k):
    if k > len(a) * len(b):
        k = len(a) * len(b)

    result = []

    num_list = [a[0]+b[0]]
    idx_list = [0]

    while k > 0:

        max_num = num_list[0]
        max_idx = 0

        for i in range(len(num_list)):
            if max_num == None or (not num_list[i] == None and num_list[i] > max_num):
                max_num = num_list[i]
                max_idx = i
        result.append(max_num)

        idx_list[max_idx] += 1
        if idx_list[max_idx] < len(b):
            num_list[max_idx] = a[max_idx] + b[idx_list[max_idx]]
        else:
            num_list[max_idx] = None

        if len(num_list) < len(a):
            num_list.append(a[len(num_list)] + b[0])
            idx_list.append(0)

        k -= 1

    return result

#9. 有序数组内相加和的top k
def arrayAddup(nums, k):
    total = reduce(lambda x, y: x + y, range(1, len(nums)))
    if k > total:
        k = total

    result = []

    num_list = [nums[0] + nums[1]]
    idx_list = [1]

    while k > 0:

        max_num = num_list[0]
        max_idx = 0

        for i in range(len(num_list)):
            if max_num == None or (not num_list[i] == None and num_list[i] > max_num):
                max_num = num_list[i]
                max_idx = i
        result.append(max_num)

        idx_list[max_idx] += 1
        if idx_list[max_idx] < len(nums):
            num_list[max_idx] = nums[max_idx] + nums[idx_list[max_idx]]
        else:
            num_list[max_idx] = None

        if len(num_list) < len(nums) - 1:
            idx_list.append(len(num_list) + 1)
            num_list.append(nums[len(num_list)] + nums[len(num_list) + 1])

        k -= 1
    
    return result

#10. 合并区间
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return 's: ' + str(self.start) + ', e: ' + str(self.end)

def get_key(x):
        return x.start

def merge(intervals):
    result = []

    if len(intervals) == 0:
        return result

    intervals.sort(key = get_key)

    for i in range(len(intervals)):
        if len(result) == 0:
            result.append(intervals[i])
        else:
            interval = intervals[i]
            if interval.start <= result[-1].end:
                result[-1] = Interval(result[-1].start, max(interval.end, result[-1].end))
            else:
                result.append(interval)

    return result

temp = [[1,3],[2,6],[8,10],[15,18],[0,2]]
intervals = []

for i in temp:
    intervals.append(Interval(i[0], i[1]))

result = merge(intervals)

for i in result:
    print(i)

