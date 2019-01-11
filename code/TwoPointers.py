#1.删除排序数组中的重复项
def removeDuplicates(nums):
    pointer = 0
    if len(nums) == 0:
        return pointer
    for i in range(1, len(nums)):
        if nums[i] != nums[pointer]:
            nums[pointer + 1] = nums[i]
            pointer += 1
    return pointer + 1
            
#2.盛最多水的容器
def maxArea(height):
    result = 0
    left = 0
    right = len(height) - 1
    while left < right:
        v = min(height[left], height[right]) * (right - left)
        result = max(result, v)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return result

#3.三数之和
def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        start = i + 1
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                result.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1] and nums[end] == nums[end + 1]:
                    start += 1
                    end -= 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
    return result

#4.颜色分类
def swap(a, b):
    return b, a
def sortColor(nums):
    start = 0
    end = len(nums) - 1
    pos = 0
    while pos <= end:
        if nums[pos] == 2:
            nums[pos], nums[end] = swap(nums[pos], nums[end])
            end -= 1
        elif nums[pos] == 0 and pos == start:
            start += 1
            pos += 1
        elif nums[pos] == 0 and pos != start:
            nums[pos], nums[start] = swap(nums[pos], nums[start])
            start += 1
        else:
            pos += 1
    print(nums)

#5.接雨水
def trap(height):
    result = 0
    max_idx = 0
    max_height = 0

    if len(height) == 0:
        return result

    for i in range(len(height)):
        if height[i] > max_height:
            max_height = height[i]
            max_idx = i

    root = height[0]
    for i in range(0, max_idx):
        if root < height[i]:
            root = height[i]
        else:
            result += root - height[i]

    root = height[-1]
    for i in range(len(height) - 1, max_idx, -1):
        if root < height[i]:
            root = height[i]
        else:
            result += root - height[i]

    return result