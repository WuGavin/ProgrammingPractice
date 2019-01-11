#1. 环形链表
def hasCycle(head):
    if head == None:
        return False

    fast = head
    slow = head

    while fast != None and fast.next != None and fast.next.next != None:
        slow = slow.next

        if fast != None and slow != None and fast == slow:
            return True

    return False

#2. 合并两个有序链表
def mergeTwoLists(l1, l2):
    head = None

    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1 == None and l2 == None:
        return head

    if l1.val > l2.val:
        head = l2
        l2 = l2.next
    else:
        head = l1
        l1 = l1.next

    temp = head

    while l1 and l2:
        if l1.val > l2.val:
            temp.next = l2
            l2 = l2.next
        else:
            temp.next = l1
            l1 = l1.next
        temp = temp.next
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2

    return head

#3. 删除链表的倒数第n个节点
def removeNthFromEnd(head, n):
    fast = head

    while n != 0:
        fast = fast.next
        n -= 1

    if fast == None:
        return head.next

    slow = head

    while fast.next != None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head

#4. 两两交换链表中的节点
def swapPairs(head):
    result = ListNode(0)

    result.next = head

    head = result

    while head.next != None and head.next.next != None:
        slow = head.next
        fast = head.next.next

        head.next = fast
        slow.next = fast.next
        fast.next = slow

        head = slow

    return result.next

#5. 环形链表II
def detectCycle(head):
    fast = head
    slow = head

    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            temp = head
            while temp != fast:
                temp = temp.next
                fast = fast.next
            return temp

    return None

#6. 复制带随机指针的链表
def copyRandomList(head):
    if head is None:
        return None
        
    temp = head
    while temp:
        node = RandomListNode(temp.label)
        node.next = temp.next
        temp.next = node
        temp = node.next
        
    temp = head
    while temp != None:
        if temp.random != None:
            temp.next.random = temp.random.next
        temp = temp.next.next
        
    new_head = head.next
    temp = head
    while temp != None and temp.next != None:
        node = temp.next
        temp.next = node.next
        temp = node
        
    return new_head








