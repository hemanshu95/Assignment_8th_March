class LinearSystemSolver:
    def Gauss(self,A,b):
        C = []
        Ans = []
        for i in A:
            C += [[j for j in i]+[b[A.index(i)]]]
        for i in range(1,len(b)):
            run = C[i-1][i-1]
            for j in range(len(b)+1):
                    C[i-1][j] /= run
            for j in range(i,len(b)):
                run = C[j][i-1]
                for k in range(len(b)+1):
                    C[j][k] -= run*C[i-1][k]
        run = C[i][i]
        for j in range(len(b)+1):
                    C[i][j] /= run                    
        C.reverse()            
        for i in range(len(b)):
            run = 0
            for j in range(len(Ans)):
                run += C[i][len(b)-1-j]*Ans[j]
            Ans.append(C[i][len(b)]-run)
        Ans.reverse()    
        return Ans
    def GaussJordan(self,A,b):
        C = []
        Ans = []
        for i in A:
            C += [[j for j in i]+[b[A.index(i)]]]
        for i in range(1,len(b)+1):
            run = C[i-1][i-1]
            for j in range(len(b)+1):
                    C[i-1][j] /= run
            for j in range(len(b)):
                if j != (i-1):
                   run = C[j][i-1]
                   for k in range(len(b)+1):
                       C[j][k] -= run*C[i-1][k]                
        for i in range(len(b)):
            Ans.append(C[i][len(b)])
        return Ans
    def matinA(self,m,n): ####called in Gauss Siedel
        from numpy import zeros,array
        A_=zeros((m,n),float)
        for i in range(m):
            for j in range(n):
                A_[i,j]=float(input('enter value at A['+str(i+1)+']['+str(j+1)+']  '))
        return A_
    def matinb(self,m):  ####called in Gauss Siedel
        from numpy import zeros,array
        b_=zeros((m),int)
        for i in range(m):
            b_[i]=int(input('enter value at b['+str(i+1)+']  '))
        return b_
    def GaussSiedel(self):
            import numpy as np
            n=int(input('order'))
            A=self.matinA(n,n)
            b=self.matinb(n)
            eps,D,L,U=np.zeros(n),np.zeros(n),np.zeros(n),np.zeros(n)
            for i in range(n) :
                eps[i]=.0000001                 
            lmt=20                                     

            for i in range(n):
                for j in range(n):
                    if i==j:
                        D[i,j]=A[i,j]
                    elif i>j:
                        L[i,j]=A[i,j]
            U=A-L-D

            for i in range(lmt):
                if np.greater(abs(np.dot(A,x)-b),eps).any():
                    q=- (np.dot(np.linalg.inv(L+D), b + np.dot(U, x)))
                    x=q
                else:
                    break
            return(x)
