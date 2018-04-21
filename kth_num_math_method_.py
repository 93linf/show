'''
Question:  f(n,m,l)= (2**n)*(3**m)*(5**l) , n,m,l  (0 to infinity) , 
find the Kth number 

Solution: 
To consider ((n+1)th number) / ( nth number)
比值>1,分数约简后必定是仅由2,3,5的幂组成;
分子中的幂指数不能>1,否则可以插入间隙不能保证是紧邻的比值;
1. 假设2 3 5 都集中在分子,考虑最小增长取 2;
2. 假设2 3 5 有两者集中在分子 ,考虑最小增长取 3/2, 5/3, (2*3)/5 ;
3. 假设2 3 5 仅一个集中在分子,考虑最小增长取 空集;

所以共得4个增长系数,按大小是 6/5 < 3/2 < 5/3 < 2
考虑一组(m，n，l)的下一个(m'，n'，l')时,遵从下述规则:
从小到大优先考虑4个增长系数,前提是能被增长系数的分子约简为整数
'''
def nextVars(mnl):	
	m2 ,n3 ,l5 = mnl 
	#	6/5
	if l5 > 0:		
		mnl = [ m2+1,  n3+1 ,l5-1]
	#   3/2
	elif m2 >0:
		mnl = [ m2-1 ,n3+1,l5 ]
	# 5/3
	elif n3 >0: 
		mnl = [ m2, n3-1,l5+1 ]
	# 2
	else:
		mnl = [m2+1, n3, l5]
	return mnl


def main(k):
	mnl =[ 0 , 0 ,0 ]
	i = 0
	while i<k:
		mnl = nextVars(mnl)
		i+=1
	calcFunction = lambda n,m,l: (2**n)*(3**m)*(5**l)
	return calcFunction(nml)
