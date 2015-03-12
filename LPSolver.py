class LPsolver:
    def solve(self, a, b, c):
        C, B, x, maxPos, minPos = [], [], [], [], []
        for i in c:
            C += [[j for j in i]]
