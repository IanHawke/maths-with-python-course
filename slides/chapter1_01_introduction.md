---
type: slides
---

# Introduction

Notes: This is a course for mathematicians, or those who want to think like one.
There's overlaps between how mathematicians think about problems and how coders
do. There's substantial differences as well. Just as coders find mathematical
language and notation useful, so do mathematicians find coding useful. This
course introduces coding - in particular, Python - from a mathematicians'
point of view.

---

# Getting output

```python
# Print something
print("Hello world")
```

```out
Hello world
```

The standard mathematical operations work in Python:

```python
print(1 + 2)
print(13.5 * 2.6 - 1.4) / 10.2
print(2**4)
```

```out
3
3.3039215686274517
16
```

Notes: Whenever we do something we're going to want to see output: to check
whether we did the right thing. The `print` function takes its input (here a
*string*, `"Hello world"`, which are characters enclosed by quotes `"`) and
displays the result to the screen. Note that `**` raises the first number to the power of the second.

---

# Comparing things

```python
print(2 > 1)
```

```out
True
```

```python
print(4 / 2 == 2)
```

```out
True
```

```python
print(2.1**3 == 9.261)
```

```out
False
```

Notes: As well as numbers (integers and floats, which are the computer equivalent of real numbers) and strings, Python also has *boolean* values, `True` and `False`. We can use comparison operators such as greater than or less than: the output will logically be either `True` or `False`. To compare if two numbers are *equal* we use two equal signs, `==`. We shall see later that a single equals sign has rather a different meaning. Note in the final example that comparing two numbers *exactly* can be dangerous, and not do what you would expect as a mathematician. It should be the case that $2.1^3 = 9.261$ exactly. However, these are real numbers which are represented by floats on a computer. Operations on floating point numbers can give very slightly different results: if you check this calculation you may see a difference in the sixteenth significant digit! This is enough to stop exact equality checks from working. We will later look at "close enough" checks.

---

# Let's practice!

Notes: Move on to some exercises.
