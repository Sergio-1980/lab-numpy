#1. Import the NUMPY package under the name np.
import numpy as np
import random as rd


#2. Print the NUMPY version and the configuration.

print (np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.rand(2,3,5)

#4. Print a.

print (a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print (b)

#7. Do a and b have the same size? How do you prove that in Python code?

print (a.shape == b.shape)

#8. Are you able to add a and b? Why or why not?

# We can´t cause the shape of de two arrays are different

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = np.add(a, c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print (d)


#12. Multiply a and c. Assign the result to e.

e = a * c

#13. Does e equal to a? Why or why not?

# no, because we are multiplying the values ​​"a" to the values ​​of "c"
# values of a[0,0,0] * values of c[0,0,0]


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty(d.shape)

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for i in range(d.shape[0]):
        for j in range(d.shape[1]):
            for k in range(d.shape[2]):
                value = d[i][j][k]
                if value > d_min and value < d_mean:
                    f[i][j][k] = 25
                elif value > d_mean and value < d_max:
                    f[i][j][k] = 75
                elif value == d_mean:
                    f[i][j][k] = 50
                elif value == d_min:
                    f[i][j][k] = 0
                else:
                    f[i][j][k] = 100


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print("-------------------------------------")
print(d)
print("-------------------------------------")
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

"""
No solucione el bonus :-(

ideas!!!

for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            for k in range(f.shape[2]):
                value = f[i][j][k]
                if value == 0:
                    f[i][j][k] = np. "A"
                elif value == 25:
                    f[i][j][k] = "B"
                elif value == 50:
                    f[i][j][k] = "C"
                elif value == 75:
                    f[i][j][k] = "D"
                else:
                    f[i][j][k] = "E"

import string

import math

num2alpha = dict(zip(range(1,27),string.ascii_lowercase))

y = f.flatten()

x = y.tolist()

w = [int(a) for a in x]

for i in w:
    print (num2alpha[i])

"""
print("-------------------------------------")
print (find)