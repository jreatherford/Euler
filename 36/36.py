def isBoolPalin(num):
    binStr = bin(num);
    x = 2
    y = len(binStr) - 1
    while (x < y):
        if binStr[x] != binStr[y]:
            return False
        x += 1
        y -= 1
    return True

total = 0;

for num in range(1,1000):
    front = str(num)
    reverse = front[::-1]
    palin1 = int(front + reverse)
    palin2 = int(front + reverse[1:len(reverse)])
    
    if isBoolPalin(palin1):
        total += palin1
    if isBoolPalin(palin2):
        total += palin2

print total
