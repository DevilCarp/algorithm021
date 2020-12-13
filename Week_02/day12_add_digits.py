class Solution:
    def addDigits(self, num: int) -> int:
        # 方法三，根据判断结果的大小来进行递归。进行写法简练
        return self.addDigits(sum([int(i) for i in str(num)])) if num > 9 else num