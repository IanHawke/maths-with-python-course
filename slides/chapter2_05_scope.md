---
type: slides
---

# Scope

Notes: When working with mathematical functions, one key convention you have to get used to is *context*. If we talk about $f(x)$ we usually mean that $x$ is some general value, which is unspecified. If we define $x$ to have a specific value and talk about $f(x)$, we're meaning the specific value returned from the function given that specific input. In mathematical writing we switch between these contexts often. As coding is a kind of communication we need to consider what a variable name means in different contexts, and what the different contexts may be.

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
