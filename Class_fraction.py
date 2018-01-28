from Fraction import Fraction,gcd 
#fra.show()
f1 = Fraction(3,2)
f2 = Fraction(5,2)
print("%s + %s = "%(f1,f2)),
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)
print(f1==f2) 	#checks only for  shallow equality i.e. 
				#whether both var reference to same object
f3 = f1 		#assigning reference of f1 to f3, i.e. both points to same object
print(f1==f3) 	#hence shallow equality is true
print(f1==f2) 

print(f1<=f2) 
print(f1>=f2)

print f1.get_num()
print f1.get_den()


