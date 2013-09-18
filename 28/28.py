current_point  = 1;
total = 1;
current_size = 3;
goal_size = 1001;

for current_size in range (3, (goal_size + 2),2):
    for current_side in range (0,4):
            current_point += (current_size - 1);
            total += current_point;
print total;