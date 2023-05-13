class Solution:
    def isHappy(self, n: int) -> bool:
        self.orig = n
        ninp = sum([int(i) ** 2 for i in list(str(n))])
        return self.recur(ninp)

    def recur(self, inp):
        if inp == 1 or inp == 7:
            return True
        elif len(str(inp)) == 1:
            return False
        else:
            ninp = sum([int(i) ** 2 for i in list(str(inp))])
            return self.recur(ninp)
