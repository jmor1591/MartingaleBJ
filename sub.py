import subprocess
import os
import math

margin_cons = 2.807 * .5 ##confidence interval of 99.5%
lower = -1
upper = 2
# Execute the command while the condition is not met
for i in range(100):
    while (lower < 0.5 < upper):
    #while (margin > 0.01):
    #for i in range(1000):
        if os.path.exists('count.txt'):
            # Open the file in read mode to read the current counts
            with open('count.txt', 'r') as file:
                lines = file.readlines()
                if len(lines) == 2:
                    enough_count, total_count = map(int, lines)
                else:
                    enough_count, total_count = 0, 0
        else:
            # Initialize counts if the file doesn't exist
            enough_count, total_count = 0, 0
        
        margin = margin_cons / max(math.sqrt(total_count), 1)
        lower = (enough_count / max(total_count,1)) - margin
        upper = (enough_count / max(total_count,1)) + margin
        # Execute the command
        subprocess.run(['python', '-m', 'BJsimulator'])
        print('(', lower, ',', upper, ') ', margin)
    
    subprocess.run(['python', '-m', 'BJsimulator'])
    print('(', lower, ',', upper, ') ', margin)

        # Update lower and upper bounds if necessary
        # Example:
        # lower = calculate_lower()
        # upper = calculate_upper()
