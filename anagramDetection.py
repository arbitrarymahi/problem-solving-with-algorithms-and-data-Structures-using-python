"""def compareString(s1,s2):
	list2 = list(s2)
	match = True
	pos1 = 0

	while pos1 < len(s1) and match is True :
		found = False
		pos2 = 0
		while pos2 < len(list2) and found is not True:
			if list2[pos2] == s1[pos1]:
				found = True
				
			else:
				pos2 += 1
				
		
	if found:

		list2[pos2]=None
	    match = True
	    
	    pos1 +=1	


	
	else:
	    match = False
	print list2
	return match

print(compareString('aaa','0aaa'))
def anagram_solution1(s1,s2):
	a_list = list(s2)
	pos1 = 0
	still_ok = True
	while pos1 < len(s1) and still_ok:
		pos2 = 0
		found = False
		while pos2 < len(a_list) and not found:
			if s1[pos1] == a_list[pos2]:
				found = True
			else:
				pos2 = pos2 + 1
		if found:
			a_list[pos2] = None
		else:
			still_ok = False
		pos1 = pos1 + 1
	return still_ok
print(anagram_solution1('ambcd8','dcmba0'))

def compareString(s1,s2):
	l1 = list(s1)
	l2 = list(s2)
	l1.sort()
	l2.sort()
	i = 0
	match = True
	while i < len(s1) and match is True:
		if l1[i] == l2[i]:
			match = True
			i+=1
		else:
			match = False


	return match

print(compareString('abdl','asdl'))"""

def anagram4(s1,s2):
	l1 = [0] * 26
	l2 = [0] * 26

	for ch in s1:
		pos = ord(ch) - ord('a')
		l1[pos] +=1

	for ch in s2:
		pos = ord(ch) - ord('a')
		l2[pos] +=1

	match = True
	i = 0

	while i < 26 and match:
		if l1[i] == l2[i]:
			match = True
			i+=1
		else:
			match = False

	return match
print(anagram4('apppe','papep'))