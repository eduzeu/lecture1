import math as math 
import matplotlib.pyplot as plt 
import numpy as np

a, b, c = input("Write the values of your coefficient: ").split()
a = float(a)
b = float(b)
c = float(c)
print("a, b, c are: {0:.2f}, {1:.2f}, {2:.2f}".format(a,b,c))


root1 = (-b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
root2 = (-b - math.sqrt(math.pow(b,2)-4*a*c))/(2*a)

print("x intercepts: ({0:.3f},0), ({1:.3f}, 0)".format(root1, root2))
print("y intercept: (0,{0:.3f})".format(c))

discriminant = math.pow(b,2)-4*a*c

if(discriminant >= 0):
    root1 = (-b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    root2 = (-b - math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
else:
    print("does not have x intercepts")



