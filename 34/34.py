
def isDigitFact(num, facts):
    total = 0;
    startingNum = num
    
    while (num >= 1):
        total += facts[num%10]
        num /= 10
        if total > startingNum:
            return False
    if (total == startingNum):
        return True
    else:
        return False
        

facts = [1] * 10
for i in range (2,10):
    facts[i] = i * facts[i-1]
    
grandTotal = 0;
for i in range (11,100000,1):
    if (isDigitFact(i,facts)):
        grandTotal += i
        
print grandTotal

