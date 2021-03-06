#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   分隔链表.py
@Time    :   2021/1/4 10:48 上午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。


示例：

输入：head = 1->4->3->2->5->2, x = 3
输出：1->2->2->4->3->5

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 将原始链表进行拆解
        # 小于x的链表记为p；大于x的链表记为q。
        # 最终进行p+x+q的链表拼接。
        p = less = ListNode(0)
        q = more = ListNode(0)
        while head:
            if head.val<x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        more.next = None
        less.next= q.next
        return p.next