#!/usr/bin/env python
# coding: utf-8

# In[1]:


# CALCULATOR
# TASK 2
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

a=int(input("enter first number: "))
b=int(input("enter second number: "))
choice=input("--------------  Enter choice from +,-,*,/ -------------    : ")
if choice == '+':
    c=a+b
    print("result = ",c)
elif choice == '-':
    c=a-b
    print("result = ",c)
elif choice == '*':
    c=a*b
    print("result = ",c)
elif choice == '/':
    c=a/b
    print("result = ",c)
else:
    print("enter valid choice")
    print(" TRY AGAIN ")
    


# In[ ]:




