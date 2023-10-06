# Exam block #2: Control Flow - Conditional Blocks and Loops

"""
1. Conditional statements
The conditional statement (the if statement) is a means allowing the 
programmer to branch the execution path and to execute (or not) 
selected instructions when a certain condition is met (or not).

2. The basic form of the if statement looks as follows:

if condition:
    instructions

3. The condition is an expression – if it evaluates to True, or to a non-zero numeric value, or to a non-empty string and is not None, 
it is fulfilled (met), and the nested instructions placed after the if are executed.

4. When the condition is not met, these instructions are skipped.

5. When there is only one instruction that should be executed conditionally, the instruction can be written in the following form:

if condition: instruction

6. For example, the following snippet prints TRUE to the screen:
"""

# counter = 1
# if counter > 0:
#     print('TRUE')
    

"""
7. The empty instruction denoted by the pass keyword can be used to indicate that no action 
should be performed in the specific context. As the if instruction syntax insists that 
there should be at least one statement after it, the following snippet does not 
affect program execution:


if condition:
    pass

8. It is suggested to use one tabulation character to make one indent level in Python code, while the 
recommended tab size (settable in virtually all code editors) is 4.

9. The else branch can be used to specify a part of the code that should be executed when the condition is not met:

if condition:
    instructions
else:
    instructions
"""

# 10. For example, the following snippet prints TRUE when the counter variable is greater than zero, and FALSE otherwise:

# counter = -1
# if counter > 0:
#     print('TRUE')
# else:
#     print('FALSE')
    
""" 
11. To check more than one condition within one conditional block, the elif branch or branches may be employed. 
In that case, not more than one if/elif branch can be executed. The else branch is optional, 
and must be the last branch.
"""

# 12. For example, the following snippet prints PLUS when the counter variable is greater than zero, MINUS when it's less than zero, and ZERO when it's equal to zero:

# counter = 1
# if counter > 0:
#     print('PLUS')
# elif counter < 0:
#     print('MINUS')
# else:
#     print('ZERO')
    

# Loops
"""
1. The while loop statement is a means allowing the programmer to repeat the execution of the selected part of the code as long the specified condition is true. The condition is checked before the loop's first turn, and therefore the loop's body may not even be executed once.

2. The basic form of the while statement looks as follows:

while condition:
    instructions
    

3. The condition is an expression – as long it evaluates to True, or to a non-zero numeric value, or to a non-empty string, it is fulfilled (met) and is not None, the nested instructions placed after the while are executed.

4. When the condition is not met, these instructions are skipped.
"""

# For example, the following snippet prints TRUE twice to the screen:
# The code snippet you provided will print "TRUE" once, not twice. 
# It prints "TRUE" when counter is greater than 0 (which happens initially when counter is 2), 
# but after printing once, it subtracts 1 from counter, and the if condition is no longer true. 
# Therefore, it won't print "TRUE" a second time.

# counter = 2
# if counter > 0:
#     print('TRUE')
#     counter -= 1

#Correct example

# counter = 2
# if counter > 0:
#     print('TRUE')
# if counter > 1:
#     print('TRUE')


"""
5. The else branch can be used to specify a part of the code that should be executed when the loop’s condition is not met:

while condition:
    instructions
else:
    instructions
"""

#For example, the following snippet prints TRUE FALSE to the screen:

# counter = 1
# while counter > 0:
#     print('TRUE', end=' ')
#     counter -= 1
# else:
#     print('FALSE')


"""
6. If the condition is met at the beginning of the loop and there is no chance that the condition value has changed 
inside the body of the loop, the execution enters an infinite loop which cannot be broken without the user's 
intervention, for example by pressing the Ctrl-C (Ctrl-Break) key combination.
"""

# For example, the following snippet infinitely prints TRUE to the screen:

# while True:
#     print('TRUE', end=' ')

""" 
7. The for loop statement is a means allowing the programmer to repeat the execution of the selected part of the 
code when the number of repetitions can be determined in advance. The for statement uses a dedicated variable 
called a control variable, whose subsequent values reflect the status of the iteration.

8. The basic form of the for statement looks as follows:

for control_variable in range(from, to, step):
    instructions


9. The range() function is a generator responsible for the creation of a series of values starting from 
from and ending before reaching to, incrementing the current value by step.

10. The invocation range(i,j) is the equivalent of range(i, j, 1)

11. The invocation range(i) is the equivalent of range(0, i)
"""

# For example, the following snippet prints 0,1,2, to the screen:

# for i in range(3):
#     print(i, end=',')


# For example, the following snippet prints 2 1 0 to the screen:

# for i in range(2, -1, -1):
#     print(i, end=' ')

"""
12. The else branch can be used to specify a part of the code that should be executed when the loop's body is not entered, 
which may happen when the range being iterated is empty or when all the range's values have already been consumed.
"""

# For example, the following snippet prints 0 1 2 FINISHED to the screen:

# for i in range(3):
#     print(i, end=' ')
# else:
#     print('FINISHED')


# For example, the following snippet prints FINISHED to the screen:

# for i in range(1,1):
#     print(i, end=' ')
# else:
#     print('FINISHED')

"""
13. The break statement can be used inside the loop's body only, and causes immediate termination of the loop's code. 
If the loop is equipped with the else branch, it is omitted.
"""

# For example, these two snippets print 0 1 to the screen:

# break inside for
# for i in range(3):
#     if i == 2:
#         break
#     print(i, end=' ')
# else:
#     print('FINISHED')



# break inside while

# i = 1
# while True:
#     print(i, end=' ')
#     i += 1
#     if i == 3:
#         break    
# else:
#     print('FINISHED')


"""
14 The continue statement can be used inside the loop's body only, and causes an immediate transition to 
the next iteration of the for loop, or to the while loop's condition check.
"""


#For example, these two snippets print 0 2 FINISHED to the screen:

# continue inside for
# for i in range(4):
#     if i % 2 == 1:
#         continue
#     print(i, end=' ')
# else:
#     print('FINISHED')



# continue inside while

# i = -1
# while i < 3:
#     i += 1
#     if i % 2 != 0:
#         continue
#     print(i, end=' ')
# else:
#     print('FINISHED')


### block exam

# 1. What is the expected output of the following code?
# planets = 1 + 1 // 2 * 3
# if planets > 0:
#     print("#")
# elif planets > 1:
#     print("##")
# else:
#     print("###")

# Hence the expression 1 + 1 // 2 * 3 evaluates to 1, and the control reaches  the very first print() invocation
# answer: #



# 2. What is the expected output of the following code?
# planets = 4 - 3 // 2 + -1
# if planets < 0:
#     print("#")
# elif planets >= 2:
#     print("##")
# else:
#     print("###")
    
#the expression 4 - 3 // 2 + -1 evaluates to 2 - this is why the control reaches the second print() invocation only.
#answer: ##

 
# 3. How many asterisk (*) does the code output to the screen

# torque = 5
# while torque > 0:
#     torque -= 3
#     print("*", end="")
# else:
#     print("*")



# 4. How many asterisk (*) does the code output to the screen

# torque = 1
# while torque < 2:
#     torque *= 2
#     print("*", end="")
# else:
#     print("*")
 

#what happens when the user runs the following code?
# power = 1
# while power != 10:
#     power *= 2
#     if power == 5:
#         continue
#     print("@", end="")
# else:
#     print("@")
    

#what happens when the user run the following code?
# power = 1
# while power < 5:
#     power += 1
#     print("@", end="")
#     if power == 3:
#        break
# else:
#     print("@")


#what happens when the user runs the following code?
# angle=0
# for i in range(5):
#     if i % 2 == 1:
#         angle += 1
# else:
#     angle -= 1
# print(angle)


#what happens when the user runs the following code?
# angle=1
# for i in range(2, 5):
#     if 2 * i > 4:
#         angle += 1
# else:
#     angle -= 1
# print(angle)


# what is the expected output of the following code?
# others = 0
# for i in range(2):
#     for j in range (2):
#         if i != j:
#             others +=1
# else:
#     others += 1
# print(others)


# what is the expected output of the following code?
# others = -1
# for i in range(1, 3):
#     for j in range (1, 2):
#         if i == j:
#             others += 1
# else:
#     others += 1
# print(others)