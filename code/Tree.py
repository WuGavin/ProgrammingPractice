#1. 对称二叉树
def judge(left, right):
    if (left == None and right != None) or (left != None and right == None) or (left.val != right.val):
        return False
    if left == None and right == None:
        return True
    return judge(left.left, right.right) and judge(left.right, right.left)

def isSymmetric(root):
    if root == None:
        return True
    return judge(root.left, root.right)

#2. 二叉树的前序/中序/后序遍历
def preTraverse(root):
    if root == None:
        return
    print(root.val)
    preTraverse(root.left)
    preTraverse(root.right)

def inTraverse(root):
    if root == None:
        return
    inTraverse(root.left)
    print(root.val)
    inTraverse(root.right)

def postTraverse(root):
    if root == None:
        return
    postTraverse(root.left)
    postTraverse(root.right)
    print(root.val)

#3. 二叉树的最大深度
def maxDepth(root):
    if root == None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

#4. 翻转二叉树
def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

#5. 平衡二叉树
def depth(root):
    if root == None:
        return 0
    return max(depth(root.left), depth(root.right)) + 1

def isBalanced(root):
    if root == None:
        return True
    return (abs(depth(root.left) - depth(root.right)) <= 1) and isBalanced(root.left) and isBalanced(root.right)


#6. 路径总合II
def find(root, sum, result, temp):
    temp.append(root.val)
    if root.left == None and root.right == None:
        if sum == root.val:
            result.append(list(temp))

    if root.left != None:
        find(root.left, sum - root.val, result, temp)
    if root.right != None:
        find(root.right, sum - root.val, result, temp)

def pathSum(root, sum):
    if root == None:
        return []
    result = []
    find(root, sum, result, [])
    return result

#7. 求根到叶子节点数字之和
def getNum(root, num, result):
    num = num * 10 + root.val
    if root.left == None and root.right == None:
        result.append(num)
    if root.left != None:
        result = getNum(root.left, num, result)
    if root.right == None:
        result = getNum(root.right, num, result)
    return result

def sumNumbers(root):
    if root == None:
        return 0
    result = getNum(root, 0, [])
    return sum(result)

#8. 二叉树的锯齿状遍历
def zigzagLevelOrder(root):
    result = []

    if root == None:
        return []

    queue = [root]
    len_cur = 1
    len_next = 0

    direction = True

    temp = []
    while len(queue) > 0:
        temp.append(queue[0].val)
        if direction:
            if queue[0].left != None:
                queue.insert(len_cur, queue[0].left)
                len_next += 1
            if queue[0].right != None:
                queue.insert(len_cur, queue[0].right)
                len_next += 1
        else:
            if queue[0].right != None:
                queue.insert(len_cur, queue[0].right)
                len_next += 1
            if queue[0].left != None:
                queue.insert(len_cur, queue[0].left)
                len_next += 1
        len_cur -= 1
        del queue[0]

        if len_cur == 0:
            direction = not direction
            len_cur = len_next
            len_next = 0
            result.append(list(temp))
            temp = []
    return result

#9. 二叉树中的最大路径和
def subpath(root, max_sum):
    if root == None:
        return 0
    left, max_sum = subpath(root.left, max_sum)
    right, max_sum = subpath(root.right, max_sum)

    curr_sum = max(left, 0) + max(0, right) + root.val
    max_sum = max(curr_sum, max_sum)
    return max(max(left, 0), max(right, 0)) + root.val, max_sum

def maxPathSum(root):
    _, result = subpath(root, -9999)
    return result

#10. 恢复二叉搜索树
def dfs(root, node_list):
    if root == None:
        return
    dfs(root.left, node_list)
    node_list.append(root)
    dfs(root.right, node_list)

def recoverTree(root):
    node_list = []
    dfs(root, node_list)

    start = 0
    end = len(node_list) - 1

    while start < end:
        if node_list[start].val < node_list[start + 1].val:
            start += 1
        elif node_list[end].val > node_list[end - 1].val:
            end -= 1
        else:
            node_list[start].val, node_list[end].val = node_list[end].val, node_list[start].val
            return 






