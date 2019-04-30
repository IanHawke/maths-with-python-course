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

```python
# This is wrong:
1.23 = x
```

```out
SyntaxError: can't assign to literal
```

Notes: There's a lot of mathematical power in giving a specific value a general name. When doing algebra you know that each variable can be replaced by a specific value, but by manipulating things at the more abstract level you can get more general solutions. To do this in code we assign a label, or name, to a value. This *variable* can now be used whenever we want its value. The notation for doing this in Python is to put the label, or variable name, on the left of an equals sign `=`, with the value you wish to assign on the right. It is important to note that the equals sign `=` is not the mathematical equality operator, and does not have the properties of equality that we expect in Mathematics. For example, putting the variable name on the right and the value on the left does not work. The `=` in Python is the *assignment operator* that labels the value with the variable name. This notation is used in many other programming languages.

---

# Assigning to variables

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

This does not mean the two values are equal!

```python
print(3 == "Hello")
```

```out
False
```

Notes: In Python you can use the same variable on any sort of value, like a sticky note. Think of picking up the note `x` from the integer `3` and move it onto the string `Hello`, and Python is perfectly happy. This again shows how a single `=` is not the mathematical equality operator. In mathematics, if $x = a$ and $x = b$ then (using *transitivity*) it must be true that $a = b$. Here we have assigned `3` the label `x` using the `=` operator. We have then removed the label `x` from `3` and assigned it to `"Hello"`. The values are completely different.

---

# Using variables

Operations can use variables: their current value is substituted:

```python
x = 1.2
y = 3.4
print(2*x + y/2)
```

```out
4.1
```

Notes: We can then mix variables and numbers or other variables in operations. This reads much more like a mathematical, algebraic expression.

---

# Variable names

Mathematicians tend to use short names:

- $n$: typically an integer;
- $x, t$: typically a real number, like space or time coordinates;
- $y, f$: typically a function;
- $A$: typically a matrix.

Programmers prefer long, descriptive names:

- `list_length`;
- `max_temperature`;
- `solve_differential_equation`;
- `stiffness_matrix`.

Notes: Mathematicians prefer short names, often a single character, as it makes it easier to read and carry out calculations and proofs with lots of terms. Lots of operations will also be implicit in mathematical notation (for example, multiplying two variables $x$ and $y$ is shown by $xy$, which is different to the single variable with two characters `xy`). This reduces the amount of reading and writing, and also the cognitive load. That is, it hides the "non-essential" details whilst doing the calculation. For programmers it is easier to build up operations step-by-step, and it is easier to avoid mistakes by using long, descriptive variable names. This makes it easier to see the purpose of any single term immediately, and tools (such as tab completion) in editors minimise the amount of typing and mistakes. Both approaches are valid, and you should practice translating between the two.

---

# Moving on...
