class Fraction:
	"""docstring fos Fraction"""
	def __init__(self, up,down):
		x = gcd(up,down)
		self.num = up/x
		self.den = down/x

	def show(self):
		#print('%d/%d'%(self.num,self.den))
		print self.num,"/",self.den

	def __str__(self):
		return str(self.num)+"/"+str(self.den)

	def __add__(self,other):
		sum_num = self.num*other.den + self.den*other.num
		sum_den = self.den*other.den
		temp = gcd(sum_num,sum_den)
		return str(sum_num/temp)+'/'+str(sum_den/temp)

	def __sub__(self,other):
		sum_num = self.num*other.den - self.den*other.num
		sum_den = self.den*other.den
		temp = gcd(sum_num,sum_den)
		return str(sum_num/temp)+'/'+str(sum_den/temp)

	def __mul__(self,other):
		sum_num = self.num*other.num
		sum_den = self.den*other.den
		temp = gcd(sum_num,sum_den)
		return str(sum_num/temp)+'/'+str(sum_den/temp)

	def __div__(self,other):

		sum_num = self.num*other.den
		sum_den = self.den*other.num
		temp = gcd(sum_num,sum_den)
		return str(sum_num/temp)+'/'+str(sum_den/temp)

	def __eq__(self,other):	
			#to check deep equality I have overriden the __eq__ fn so that 
			#instead of checking reference it compares values and 
			#returns True if both matches 
		first_num = self.num*other.den
		second_num = self.den*other.num
		
		return first_num == second_num

	def __lt__(self,other):	
			
		first_num = self.num*other.den
		second_num = self.den*other.num
		
		return first_num < second_num

	def __le__(self,other):	
			
		first_num = self.num*other.den
		second_num = self.den*other.num
		
		return first_num <= second_num

	def __gt__(self,other):	
			
		first_num = self.num*other.den
		second_num = self.den*other.num
		
		return first_num > second_num

	def __ge__(self,other):	
				
		first_num = self.num*other.den
		second_num = self.den*other.num
		
		return first_num >= second_num

	def __ne__(self,other):	
			
		first_num = self.num*other.den
		second_num = self.den*other.num
		
		return first_num != second_num


	def get_num(self):
		return(self.num)

	def get_den(self):
		return(self.den)

def gcd(m,n):
	while (m % n != 0):
		temp = m % n
		m = n
		n = temp
	return n

