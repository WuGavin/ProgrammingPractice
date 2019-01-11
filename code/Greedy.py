#1. 买卖股票的最佳时机II
def maxProfit(prices):
    result = 0

    for i in range(len(prices)):
        if i > 0 and prices[i] - prices[i - 1] > 0:
            result += prices[i] - prices[i - 1]

    return result

#2. 加油站
def canCompleteCircuit(gas, cost):
    total_gas = 0
    current_gas = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            start = i + 1
            current_gas = 0

    return -1 if total_gas < 0 else start

#3. 跳跃游戏
def canJump(nums):
    reach = 0

    for i in range(len(nums)):
        if reach < i or reach >= n - 1:
            break
        reach = max(reach, nums[i] + i)

    return reach >= len(nums) - 1

#4. 分发糖果
def candy(ratings):
    result = [1 for i in range(len(ratings))]

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1] and result[i] <= result[i - 1]:
            result[i] = result[i - 1] + 1

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and result[i] <= result[i + 1]:
            result[i] = result[i + 1] + 1

    return sum(result)

#5. 跳跃游戏II
def jump(nums):
    result = 0
    
    pre_pos = 0
    cur_pos = 0

    for i in range(len(nums) - 1):
        cur_pos = max(cur_pos, nums[i] + i)
        if pre_pos == i:
            pre_pos = cur_pos
            result += 1

            if cur_pos >= len(nums) - 1:
                break

    return result