# Check Tutorial tab to know how to to solve.

# Task
# Read an integer n . For all non-negative integers i < n, print i2. See the sample for details.

# Input Format

# The first and only line contains the integer, n.

# Constraints
# 1 <= n <= 20 

# Output Format

# Print n lines, one corresponding to each i .

# Sample Input 0

# 5
# Sample Output 0

# 0
# 1
# 4
# 9 
# 16


import math

n = int(input())

for i in range(0, n):
    print(pow(i, 2))
