class Integrate:
	def solve(self,order,coeff,method):
		def f(x):
			s=0
			for i in range(order+1):
				s=s+(coeff[i]*(x**(order-i)))
			return s
		if method=='trapezoid':
			a=float(input('Lower limit: '))
			b=float(input('Upper limit: '))
			n=int((b-a)/0.001)
			x_values=[a]
			for i in range(1,n):
				x_values.append(float(str(x_values[0]+(0.001*i))[:5]))
			x_values.append(b)
			def trapezoid_sol(f,x_values,n):
				s=0
				for i in range(1,n):
					s=s+f(x_values[i])
				s=s*2
				s=s+(f(x_values[0])+f(x_values[n]))
				ans=((x_values[n]-x_values[0])*s)/(2*n)
				return ans
			return trapezoid_sol(f,x_values,n)
		elif method=='simpson':
			a=float(input('Lower limit: '))
			b=float(input('Upper limit: '))
			n=int((b-a)/0.0005)
			x_values=[a]
			for i in range(1,n):
				x_values.append(float(str(x_values[0]+(0.0005*i)[:5]))
			x_values.append(b)
			def simpson_sol(f,x_values,n):
				s1=0
				s2=0
				s3=0
				for i in range(1,n,2):
					s1+=f(x_values[i])
				s1*=4
				for i in range(2,n,2):
					s2+=f(x_values[i])
				s2*=2
				s=s+(f(x_values[0])+f(x_values[n])+s1+s2)
				ans=((x_values[n]-x_values[0])*s)/(3*n)
				return ans
			return simpson_sol(f,x_values,n)
