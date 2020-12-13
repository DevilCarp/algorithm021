class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # 左括号入栈，右括号出栈
        # 若左括号入栈后的个数大于1，则不为最左边的左括号，加入结果（
        # 若右括号出栈后，栈的个数大于0，右括号不是最右边的右括号，加入结果）
        stack = []
        result = ''
        for i in S:
            if i =="(":
                stack.append(i)
                if len(stack)>1:
                    result+='('
            else:
                stack.pop()
                if len(stack)>0:
                    result+=')'
        return result