#!/Users/lyjsmac/opt/anaconda3/bin/python3.8
# -*- encoding: utf-8 -*-
'''
@File    :   最后一块石头的重量.py
@Time    :   2021/1/4 10:45 上午
@Author  :   little_carp
@Contact :   woshiliyujian@gmail.com
@Desc    :   None
'''

# here put the import lib
'''
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为x 和y，且x <= y。那么粉碎的可能结果如下：

如果x == y，那么两块石头都会被完全粉碎；
如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。



示例：

输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。

'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)>2:
            # 先对数组进行排序
            stones.sort(reverse = False)
            # [2,7,4,1,8,1] -> [1, 1, 2, 4, 7, 8]
            x = stones[-2]
            y = stones[-1]
            if x==y:
                stones.remove(x)
                stones.remove(y)
            elif x !=y:
                stones.remove(x)
                stones.remove(y)
                stones.append(y-x)
            return self.lastStoneWeight(stones)
        elif len(stones)==2:
            stones.sort(reverse = False)
            return stones[1]-stones[0]
        else:
            return stones[0]