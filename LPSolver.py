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
        while True:
            maxPos, minPos = [], []
            for i in range(len(a)):
                sum = 0
                for j in range(len(b)):
                    sum += C[j][i]*B[j]
                maxPos += [a[i]-sum]
            counter = 0
            for i in maxPos:
                if i <= 0:
                     counter += 1
            if counter == len(a):
                 break
            index1 = maxPos.index(max(maxPos))    
            for i in range(len(b)):
                if C[i][index1] != 0:
                     minPos += [b[i]/C[i][index1]]
                elif b[i] > 0:
                    minPos += ["infinity"]
                else:
                    minPos += ["-infinity"]
            counter = 0
            for i in minPos:
                if i != "infinity":
                    if i == "-infinity":
                        counter += 1
                    elif i <= 0:
                        counter += 1
            if counter == len(b):
                return " problem is unbounded "
            z=[]
            for i in minPos:
                if i!="infinity" and i!="-infinity":
                    if i>0:
                        z += [i]
            index2 = z.index(min(z))+1
            counter = 0
            for i in minPos:
                if i!="infinity" and i!="-infinity":
                    if i > 0:
                        counter += 1
                if counter == index2:
                    index2 = minPos.index(i)
                    break
            B[index2] = a[index1]            
            b[index2] = b[index2]/C[index2][index1]
            run = C[index2][index1]
            for i in range(len(a)):
                C[index2][i] = C[index2][i]/run    
            for i in range(len(b)):
                if i != index2:
                    num = C[i][index1]
                    for j in range(len(a)):
                        C[i][j] -= num*C[index2][j]
                    b[i] -= num*b[index2]       
        sum = 0
        for i in range(len(b)):
            sum += B[i]*b[i]
        return sum
