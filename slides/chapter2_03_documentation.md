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

# Let's practice!

Notes: Move on to some exercises.
