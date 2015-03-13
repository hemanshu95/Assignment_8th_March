class Interpolate:
    
    def solve(self,A,B,method):
        if(method=="newton"):
            return (self.Newton(A,B))
        else:
            return (self.Lagrange(A,B))
    
    def Lagrange(self,A,B):                                                
       
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(A)                                                           
        w=(-1*A[0],1)                                                      
        for i in range(1,n):
            w=P.polymul(w,(-1*A[i],1))                                    
        result=array([0.0 for i in range(len(w)-1)])                    
        derivative=P.polyder(w)                                             
        for i in range(n):
            result+=(P.polydiv(w,(-1*A[i],1))[0]*B[i])/P.polyval(A[i],derivative)   
        return(list(result)) 
        
    def Newton(self,A,B):                                                   
       
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(A)                                                            
        mat=[[0.0 for i in range(n)] for j in range(n)]                    
        for i in range(n):                                                 
            mat[i][0]=B[i]
        for i in range(1,n):                                               
            for j in range(n-i):
                mat[j][i]=(mat[j+1][i-1]-mat[j][i-1])/(A[j+i]-A[j])
        res=array((mat[0][0],))                                          
        for i in range(1,n):
            prod=(-1*A[0],1)                                               
                                                                            
            for j in range(1,i):
                prod=P.polymul(prod,(-1*A[j],1))                              
            res=P.polyadd(res,array(prod)*mat[0][i])                  
        return (list(res))                                               

apx=Interpolate()                                                          
for method in ["newton","lagrange"]:
    sol=apx.solve([1,2,3],[0,-1,0],method)
    print(sol)
               
    

   
