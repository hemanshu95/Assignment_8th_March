import numpy as np
import itertools as it
class Interpolate:
    def __init__(self):
        self.f=None
        self.xi=None
        self.a=None
        self.n=None

    def solve(self,fxi,xv):
        self.f=np.array(fxi,float)
        self.xi=np.array(xv,float)
        self.n=self.xi.shape[0]-1
        self.a=np.array([0]*(self.n+1),float)
        for i in range(self.n+1):
            r=float(1)
            for j in range(self.n+1):
                if i!=j:
                    r=r*(self.xi[i]-self.xi[j])
            sum1=self.f[i]
            t=[self.xi[k] for k in range(self.n+1) if k!=i  ]
            for z in range(self.n+1):
                sum1=self.f[i]
                if z<self.n:
                    sum1=sum1*pow(-1,self.n-z)*sum([np.product(np.array(q,float)) for q in it.combinations(t,self.n-z)])
                sum1=sum1/r
                self.a[z]=self.a[z]+sum1
        for i in range(self.n,-1,-1):
            print(self.a[i],'x^',i,' + ',end='')
sol=Interpolate()
sol.solve([1,2,4],[1,0,2])
##The second part of this was not understood by the author of the Appendix-D ,So the whole Appendix-D was done by some other author. 





