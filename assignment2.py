#!/usr/bin/env python
# coding: utf-8

# # Problem 1
# 
# We know that a quadratic equation with coefficients $a, b$, and $c$ of the form
# 
# $$
# a x^2 + b x + c = 0,
# $$
# 
# has the two solutions
# 
# $$
# x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}.
# $$
# 
# Uncomment the two lines of code below and complete the function to return the correct solutions to the quadratic equation given `a`, `b`, and `c` as arguments to the function.
# 
# **Notes:** 
#  
#  * A comment in Python starts with `#`.  This means these lines will not be run during the execution of the function.  The word *uncomment* in the context of programming means to delete the `#` and make these lines active in the program.
#  
#  * Recall that the square root a variable $x$, i.e. $\sqrt{x}$, can also be written as $x^{0.5}$.
#  
#  * The standard [order of operations](https://en.wikipedia.org/wiki/Order_of_operations) for mathematics applies here.
#  
#  * Recall that the code below only *defines* the function.  You have to *execute* the function on a separate line, defining the arguments `a`, `b`, and `c` as numbers, to test the functions output.
# 
# 

# In[20]:


def quadratic_equation(a, b, c):
    ans1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    ans2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    
    return (ans1, ans2)


# # Problem 2
# 
# Uncomment the line of code below and write a string that is formatted to return
# 
# ```python
# "Hello, World! My name is John!"
# ```
# 
# where `"John"` can be replaced with any `name` that is given as an argument to the function.  For example, calling the function as
# 
# ```python
# hello_world_with_name("Romeo")
# ```
# 
# will return
# 
# ```python
# "Hello, World! My name is Romeo!"
# ```
# 
# and calling the function as
# 
# ```python
# hello_world_with_name("Juliet")
# ```
# 
# will return
# 
# ```python
# "Hello, World! My name is Juliet!"
# ```

# In[47]:


def hello_world_with_name(name):
    
    ans = f"Hello, World! My name is {name}!"
    
    return(ans)


# In[ ]:




