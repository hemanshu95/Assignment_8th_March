class LPsolver:
    def solve(self, a, b, c):
        C, B, x, maxPos, minPos = [], [], [], [], []
        for i in c:
            C += [[j for j in i]]
        x= [0 for j in range(len(a))]    
        for i in range(len(b)):
            C[i] += [0 for i in range(len(b))]
            C[i][len(a)+i] = 1
        a += [0 for i in range(len(b))]
        B = [0 for i in range(len(b))]    
