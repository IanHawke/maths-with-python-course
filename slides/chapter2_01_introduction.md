---
type: slides
---

# Introduction

Notes: In chapter 1 we saw how to use Python as a calculator. We also saw how we can do more complex calculations using a package: we `import` the package and then we can use functions and variables defined in that package. For example, we looked at the `math` package which contains the `sin` function as `math.sin`, and contains the important mathematical constant $\pi$ as `math.pi`. We want to create our own functions to mirror the functions that we build and use as mathematicians.

---

# What is a **mathematical** function?

A function is a black box that takes some input and gives some output.
$$
\begin{aligned}
f(x) &= 2 x. \\\\
f: x &\to 2 x. \\\\
f: \mathbb{R} &\to \mathbb{R}.
\end{aligned}
$$
This is the same function written three ways. Sometimes see two used together, as:
$$
\begin{aligned}
f: \mathbb{R} &\to \mathbb{R}, \\\\
f(x) &= 2 x.
\end{aligned}
$$

Notes: A function takes some input and returns some output. We can write this mathematically in many different ways. The first form is standard, and implies a lot without saying it explicitly. The second form gives the same information but is slightly more explicit. They say that the *name* of the function is $f$. They say that the *input* to the function is $x$. Whilst it is not explicit, we might *expect* that $x$ is a real number (although, in principle, it could be a complex number, or a vector, or some other mathematical structure). The *output* appears on the right of the equals sign (first form) or arrow (second form), and explicitly says how it is linked to the input. The final form is much more explicit in terms of saying what the input and output *are* (real numbers), but silent on how the output is calculated from the input. We can (and, mathematically, *should*) use two forms together to be completely explicit as to what and how a function does.

---

# What is a **computational** function?

A function is a piece of code that takes some input and gives some output.

```python
def f(x):
    return 2 * x
```

To use a function we give it a value:

```python
f(3.2)
```

```out
6.4
```

Notes: A function takes some input and returns some output. In Python we say that we are going to **define** a function using the keyword `def`. The *name* of the function is the string immediately following the keyword `def`. In this case, to match the previous slide, we have used `f`. The names of functions should obey the same rules as the names of variables: start with a letter, only use letters, numbers, and underscores, and be lowercase. The *input* appears within the brackets. The input `(x)` specifies the variable name that will be used *within the function*. As with any Python variable, when actually used, the value that the Python variable has is substituted. The definition of the function *output* follows after the colon, `:`, and is indented by four spaces. We can take as many steps as we like, but every step must be indented by four spaces. When we have computed the output (here `2 * x`) we send it back to the place that called the function by using the `return` keyword. Once the function has `return`ed its output, anything else within the function is ignored.

---

# Converting angles

Suppose we have an angle in degrees but want it in radians.

```python
import math

def degrees_to_radians(theta_d):
    theta_r = theta_d * math.pi / 180.0
    return theta_r
```

Test it, remembering $90^{\circ} = \pi / 2 \simeq 1.5708$.

```python
print(degrees_to_radians(90.0))
```

```out
1.5707963267948966
```

Notes: Here we have a slightly longer example. We want to convert an angle from degrees to radians (as mathematicians, by convention, measure angles in radians). We know that 180 degrees corresponds to $\pi$ radians. So, given the angle in degrees, we multiply by $\pi$ and divide by 180. Doing this once is fine: to do it many times it's best to use a function. We get the value of $\pi$ from the `math` library. We define a function called `degrees_to_radians`, which is an explanatory name. We say that the input, `theta_d`, is the angle in degrees. We compute the angle in radians, `theta_r`, using the formula specified in words above. Finally we `return` our angle in radians. Note that each line within the function is indented four spaces.

---

# Let's practice!

Notes: Move on to some exercises.
