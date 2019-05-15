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

# The `while` loop

What is the smallest $n$ for which $(15 n)^{\circ} > 1$ radian?

Predict what the following code will do, then try it yourself:
```python
theta_r = 0
n = 0
while theta_r < 1:
    n = n + 1
    theta_r = degrees_to_radians(15 * n)
    print("For n =", n, "theta =", theta_r, "radians")
print("Loop done. n =", n)
```

```out
For n = 1 theta = 0.2617993877991494 radians
For n = 2 theta = 0.5235987755982988 radians
For n = 3 theta = 0.7853981633974483 radians
For n = 4 theta = 1.0471975511965976 radians
Loop done. n = 4
```

Notes: To repeat a task we can put it inside a `while` loop. This repeats the task while a condition is met. In the problem here, the condition is that the angle is less than $1$ radian: once that is *not* true, we have found the value of $n$ we want. The syntax is similar to Python functions seen in Chapter 2. We start with the keyword `while` followed by the condition (`theta_r < 1`) that must be met for the loop to continue. The colon `:` indicates the end of the condition and the start of the loop, which contains the steps that make up the task to be repeated. Each of these steps is indented by $4$ spaces. When we are done with the loop we stop indenting the code. In this example, the function is called $4$ times, and the `print` inside the loop called $4$ times as well. The `print` outside the loop is only called once, when the loop has finished.

---

# The `for` loop

If we want to look at a fixed number of steps, we can use a `for` loop. Again, predict what the following code will do, then try it yourself:
```python
steps = 3, 4, 5
for n in steps:
    theta_r = degrees_to_radians(15 * n)
    print("For n =", n, "theta =", theta_r, "radians")
print("Loop done.")
```

```out
For n = 3 theta = 0.7853981633974483 radians
For n = 4 theta = 1.0471975511965976 radians
For n = 5 theta = 1.3089969389957472 radians
Loop done.
```

Notes: The `while` loop is useful when you want to repeat something but you don't know how many times. However, it requires some setting up (the steps before the loop starts), and you need to take care to ensure the loop stops. Proving mathematically that an algorithm *must* stop is hard, and in some cases impossible. Instead, we can think about repeating a task for all members of a set, or a vector, or some other mathematical structure that has more than one "thing", but has finite size. For this we can use a `for` loop. Here we define a variable `steps` that holds *multiple* values, `3, 4, 5`. We will look at this later. Next, we loop over the values contained in the variable. The syntax is again similar to `while` loops and to functions. We start with the keyword `for`. This is followed by defining a variable `n` whose value is set to each value within the structure `steps`. That is, the first time through the loop `n` is set to `3`. The next time it is set to `4`, and the final time to `5`. As the value of `n` only makes sense within the loop, where the code is indented by $4$ spaces, we do not refer to it in the `print` statement outside the loop.

---

# Let's practice!

Notes: Move on to some exercises.
