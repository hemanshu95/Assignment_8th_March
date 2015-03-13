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
               
    

   
