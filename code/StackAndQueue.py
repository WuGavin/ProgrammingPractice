#1.有效的括号
def match(a, b):
    if a == '(' and b == ')':
        return True
    if a == '[' and b == ']':
        return True
    if a == '{' and b == '}':
        return True
    return False

def isValid(s):
    stack = []

    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if len(stack) == 0 or not match(stack[-1], i):
                return False
            else:
                stack.pop()
    return len(stack) == 0

#2.逆波兰表达式求值
def judge(s):
    if s == '+' or s == '-' or s == '*' or s == '/':
        return True
    return False

def calc(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    else:
        if a * b < 0:
            return (-(-a / b))
        else:
            return a / b

def evalRPN(tokens):
    nums = []

    for i in tokens:
        if not judge(i):
            nums.append(int(i))
        else:
            b = nums[-1]
            nums.pop()
            a = nums[-1]
            nums.pop()
            nums.append(int(calc(a, b, i)))
    return nums[-1]

#3.堆栈实现队列，队列实现堆栈
class MyStack(object):

    def __init__(self):
        self.queue_in = []
        self.queue_out = []

    def push(self, x):
        while len(self.queue_out) > 0:
            self.queue_in.append(self.queue_out.pop(0))
        self.queue_out.append(x)
        while len(self.queue_in) > 0:
            self.queue_out.append(self.queue_in.pop(0))

    def pop(self):
        return self.queue_out.pop(0)
        

    def top(self):
        return self.queue_out[0]
        

    def empty(self):
        return len(self.queue_out) == 0


class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        while len(self.stack_out) > 0:
            self.stack_in.append(self.stack_out.pop())
        self.stack_out.append(x)
        while len(self.stack_in) > 0:
            self.stack_out.append(self.stack_in.pop())

    def pop(self):
        return self.stack_out.pop()
        

    def peek(self):
        return self.stack_out[-1]
        

    def empty(self):
        return len(self.stack_out) == 0

#4.最长的有效括号
def longestValidParentheses(tokens):
    stack = []
    result = 0

    start = 0
    for i in range(len(tokens)):
        if tokens[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                start = i + 1
            else:
                stack.pop()
                if len(stack) == 0:
                    result = max(result, i - start + 1)
                else:
                    result = max(result, i - stack[-1])
    return result

#5.柱状图中的最大矩形
def largestRectangleArea(nums):
    result = 0
    stack = []
    nums.append(0)

    for i in range(len(nums)):
        l = 1
        while(len(stack) > 0 and nums[stack[-1]] >= nums[i]):
            l = stack[-1]
            stack.pop()
            v = nums[l] * (i if len(stack) == 0 else i - stack[-1] - 1)
            l += 1
            result = max(result, v)
        stack.append(i)
    return result





