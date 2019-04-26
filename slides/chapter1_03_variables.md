---
type: slides
---

# Variables

Notes: Working just with numbers doesn't give us much abstraction. As mathematicians we know the power of, for example, algebra: being able to refer to a "general thing". We can do something similar in code.

---

# Assigning to variables

A variable is a label that we can put on a value:

```python
# Define a variable
x = 1.23
print(x)
```

```out
1.23
```

In Python the label can be moved from one thing to another without worry:

```python
x = 3
print(x)
x = "Hello"
print(x)
```

```out
3
"Hello"
```

Operations can use variables: their current value is substituted:

```python
x = 1.2
y = 3.4
print(2*x + y/2)
```

```out
4.1
```

Notes: There's a lot of mathematical power in giving a specific value a general name. When doing algebra you know that each variable can be replaced by a specific value, but by manipulating things at the more abstract level you can get more general solutions. To do this in code we assign a label, or name, to a value. This *variable* can now be used whenever we want its value. In Python you can use the same variable on any sort of value, like a sticky note: pick up the note `x` from the integer `3` and move it onto the string `Hello`, and Python is perfectly happy. We can then mix variables and numbers or other variables in operations, like the last mathematical operation.

---

# Moving on...
