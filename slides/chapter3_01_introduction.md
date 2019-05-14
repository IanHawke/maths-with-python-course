---
type: slides
---

# Introduction

Notes: In chapter 2 we built a function that converts degrees to radians. This works very well for a single calculation. However, it also allows us to ask more complex questions, which require more complex steps to solve.  We can often built that complexity up by doing very similar things over and over again, in a *loop*.

---

# The first angle

We wrote a function:
```python
def degrees_to_radians(theta_d):
  """
  Convert an angle from degrees to radians.
  """
```

What is the smallest $n$ for which $(15 n)^{\circ} > 1$ radian?

Try:
```python
print(degrees_to_radians(15 * 1))
print(degrees_to_radians(15 * 2))
print(degrees_to_radians(15 * 3))
print(degrees_to_radians(15 * 4))
```

```out
0.2617993877991494
0.5235987755982988
0.7853981633974483
1.0471975511965976
```

Notes: Using a function once to get a specific result saves us having to think about the internals of the function and allows us to do more complex tasks. Using a function repeatedly to answer a question is one more complex task. Here we do it by hand. We want to know what the first multiple of $15^{\circ}$ that is greater than $1$ radian. To do this we use our function, defined in the last chapter, to compute the angle in radians for each multiple of $15^{\circ}$. This means calling the function ourselves, repeatedly. This could be error-prone and wastes time for us. Instead we should make the computer do this.

---

# Let's practice!

Notes: Move on to some exercises.
