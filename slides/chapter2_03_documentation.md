---
type: slides
---

# Documentation

Notes: Functions by themselves often need explanation. As mathematicians we bundle together a lot of complexity and hide it within a function, either so we can reason about it at a more abstract level, or so that we can do a set of steps many times without worrying about the details. However, in hiding away this complexity we may forget important points.

---

# What does a function *do*?

We defined a function

```python
import math

def f(t1):
    t2 = t1 * math.pi / 180.0
    return t2
```

What did it do, again? How can we make it obvious?

Notes: This is the function that converted angles from degrees to radians. However, the variable and function names and now short and not explanatory. You immediately see the benefit of using longer, more verbose names. However, it's not only the names that helped. On the previous slide we had, side by side, an explanation of the formula for doing the conversion. Here we only have the formula. How can we be sure it's correct?

---

# Docstrings

Python functions can have explanations built in.

```python
import math

def degrees_to_radians(theta_d):
    """
    Convert an angle from degrees to radians. As pi radians is 180 degrees,
    the conversion formula is theta_r = theta_d * pi / 180.

    Parameters
    ----------

    theta_d: float
        Angle in degrees

    Returns
    -------

    theta_r: float
        Angle in radians
    """
    theta_r = theta_d * math.pi / 180.0
    return theta_r
```

This can be inspected. Try
```python
help(degrees_to_radians)
```

Notes: A string placed immediately after the line defining the function, before the indented lines, is called a *docstring*. If three quotes are used rather than one it can extend over multiple lines. The first line of the docstring should say what the function does, briefly. After that we can add more information, specifying what the expected input and output means, and what domain(s) they are expected to come from. Compare with how we discussed the notation for a *mathematical* function. This documentation should help you understand what the function does and how it should be used. It can also be inspected directly from within Python, so you never need to look at the code again. Within pure Python use the `help` command: within IPython you can type the function name followed by `?`.

---

# Scope

What is known when?

```python
import math

# Define theta_r in global, outer context
theta_r = 1
theta_d = 1

def degrees_to_radians(theta_d):
    # Define theta_r from theta_d in local, inner context.
    # The value of theta_r will not match that in the global context.
    # However, it won't alter the value of theta_r in the global context.
    theta_r = theta_d * math.pi / 180.0
    return theta_r

theta_radians = degrees_to_radians(theta_d)
# Check that theta_r still has the global value of 1, defined at the top.
print(theta_r, theta_radians)
```

```out
1 0.017453292519943295
```

Notes: When working with mathematical functions, one key convention you have to get used to is *context*. If we talk about $f(x)$ we usually mean that $x$ is some general value, which is unspecified. If we define $x$ to have a specific value and talk about $f(x)$, we're meaning the specific value returned from the function given that specific input. In mathematical writing we switch between these contexts often. In coding, each variable has a specific value **all** of the time. However, we write functions *as if* they could take a general value.  The same variable name can be used in different contexts here as well: either in the "global", outer, context (where `theta_r=1`), or the "local" context inside the function (where `theta_r` is computed from `theta_d`). In programming terms, this context dependence is called *scope*: each variable name is associated with one single value, but depending on where you are in the code - which context - the specific value can change. Python always looks at local contexts first.

---

# Let's practice!

Notes: Move on to some exercises.
