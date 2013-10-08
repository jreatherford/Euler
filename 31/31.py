def findCombos(goal, max, values):
    total = 0
    if (max == (len(values) - 1)):
        return 1
    elif (max == 0):
        return  (1 + findCombos(goal, max+1, values))
    else:
        for i in range (0, goal/values[max]+1):
            new_goal = goal-(i*values[max])
            total += findCombos(new_goal, (max+1), values)
        return total

#------------------------------------------------------------
values = [200,100,50,20,10,5,2,1]
print findCombos (200,0,values)
