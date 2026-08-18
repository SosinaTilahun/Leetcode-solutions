class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    # Division truncating toward zero
                    if a * b < 0:
                        stack.append(-(abs(a) // abs(b)))
                    else:
                        stack.append(abs(a) // abs(b))

            else:
                stack.append(int(token))

        return stack[-1]