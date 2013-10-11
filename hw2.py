# Alexei McConville
# mccale19
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# 
import hw2_test
a = 0
b = 1
while (b <= hw2_test.n):
    a = (a + b)
    b = (b + 1)
print a

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

for y in range (2, 10):
    print (1/float(y))

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range (1, (n + 1)):
    triangular = (triangular + i)
print "triangular number", n, "via loop:", triangular
print "Triangular number", n, "Via formula:", ((n*(n+1))/2)

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
x = 1
for i in range (1, (n + 1)):
    x = (x * i)
print x

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

n = 10
x = 1
for i in range (1, (n + 1)):
    x = (x * i)
    print x

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

n = 10
z = 1
v = 1
for i in range (1, (n +1)):
    z = (z * i)
    w = 1.0/z
    v = v + w
print v

###
### Tutor: Alex
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
