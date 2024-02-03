class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            if not stk or ast > 0:
                stk.append(ast)
            else:
                while True:
                    if not stk or stk[-1] < 0:
                        stk.append(ast)
                        break
                    elif stk[-1] == -ast:
                        stk.pop()
                        break
                    elif stk[-1] > -ast:
                        break
                    else:
                        stk.pop()
        return stk
