#1. 只出现一次的数字
def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result

#2. 缺失数字
def missingNumber(nums):
    result = 0

    for i in range(len(nums)):
        result = result ^ (i + 1) ^ num

    return result

#3. 只出现一次的数字II
def singleNumberII(nums):
    result = 0

    for i in range(32):
        num_ones = 0

        for num in nums:
            temp = (num >> i) & 1

            if temp == 1:
                num_ones += 1

        if num_ones % 3 == 1:
            result |= 1 << i
    #第一位是符号位，如果得到的数超过了最大的正整数，说明是一个负数，按如下操作即可
    if result >= 2 ** 31:
        result -= 2 ** 32
    return result

#4. 求众数
def majorityElement(nums):
    #数每个bit上的1的个数，如果1的个数大于0的个数，那众数在这一位上必然位1
    result = 0

    for i in range(32):
        num_ones = 0
        num_zero = 0

        for num in nums:
            temp = (num >> i) & 1

            if temp == 1:
                num_ones += 1
            else:
                num_zero += 1

        if num_ones > num_zero:
            result |= 1 << i

    if result >= 2 ** 31:
        result -= 2 ** 32

    return result




