__author__ = 'hemanshu'
import numpy as np
class LPsolver:
    def __init__(self):
        self.x=None
        self.a=None
        self.b=None
        self.c=None
        self.n=None
        self.m=None
        self.B=None
        self.S=None
        self.maxpos=None
        self.minpos=None

    def init_the_table(self,objective,constraints_value,constraints):
        self.x=np.array([0]*10,float)
        self.a=np.array(objective,float)
        self.b=np.array(constraints_value,float)
        self.c=np.array(constraints,float)
        self.n=np.size(self.a)
        self.m=np.size(self.b)
        self.B=np.array([0]*self.m,float)
        self.S=np.array([[0]*self.m]*self.m,float)
        for i in range(self.m):
            self.S[i][i]=1
        self.maxpos=np.array([0]*(self.m+self.n),float)
        self.minpos=np.array([0]*self.m,float)

    def solve(self,option, objective,constraints_value, constraints):
        self.init_the_table(objective,constraints_value,constraints)
        print(self.S,option)
        flag=0
        while flag==0:
            for i in range(self.n):
                self.maxpos[i]=self.a[i]
                for j in range(self.m):
                    self.maxpos[i]=self.maxpos[i]-(self.c[j][i]*self.B[j])
                print(self.maxpos[i])
            for i in range(self.m):
                self.maxpos[i+self.n]=0
                for j in range(self.m):
                    self.maxpos[i+self.n]=self.maxpos[i+self.n]-(self.S[j][i]*self.B[j])
                print(self.maxpos[i+self.n])
            vm=np.array([0]*self.m,float)

            vi=np.argmax(self.maxpos)
            max_pos_v=np.max(self.maxpos)


            if max_pos_v<=0:
                break
            if vi<self.n:
                for i in range(self.m):
                    vm[i]=self.c[i][vi]

            print()
            for i in range(self.m):
                if vm[i]>0:
                    self.minpos[i]=self.b[i]/vm[i]
                else:
                    self.minpos[i]=self.b[i]*float('inf')
                print(self.minpos[i])


            flag=1




sol=LPsolver()
sol.solve('hello',[1,3],[10,5,4],[[1,2],[1,0],[0,1]])
