# Baseball Game
class Solution(object):
    def calPoints(self, operations):
        total = []
        for ops in operations:
            if ops.lstrip('-').isdigit():
                total.append(int(ops))

            elif ops in ['C']:
                total.pop(-1)

            elif ops in ['D']:
                x = 2 * total[-1]
                total.append(int(x))

            elif ops in ['+']:
                y = total[-1] + total[-2]
                total.append(int(y))

            else:
                 return False

        return sum(total)