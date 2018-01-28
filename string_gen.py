import random
import string
'''
print(random.choice('mahendrai') for _ in range(3))
test_str = 'methinks it is like a weasel'
str1 = ''
count = 0
while (str1 != test_str) :
    print (str1)
'''

def generate_string():
    return ''.join(random.choice(string.ascii_lowercase + ' ') for _ in range(27))

def score(realStr, genStr):

    points = 0
    for i in range(27):
        if realStr[i]== genStr[i]:
            points += 1
    return points/len(realStr)

def main():
    realStr = 'methinks it is like a weasel'
    best_str = ""
    best_score = 0
    testStr = generate_string()
    points = score(realStr, testStr)
    loopcount = 0
    while best_score != 1:
        if points > best_score:
            print(best_score, best_str,sep=' --->> ')
            best_score = points
            best_str = testStr

        testStr = generate_string()
        points = score(realStr, testStr)

        if loopcount == 1000000:
            loopcount =0
            print("1 million loops")
        loopcount += 1
main()
