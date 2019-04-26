---
type: slides
---

# Introduction

This is a course for mathematicians, or those who want to think like one.
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

Whenever we do something we're going to want to see output: to check whether we
did the right thing. The `print` function takes its input (here a *string*,
`"Hello world"`, which are characters enclosed by quotes `"`) and displays the
result to the screen.

---

# Python as calculator

The standard mathematical operations work in Python:

```python
print(1+2)
print(13.5*2.6-1.4)/10.2
print(2**4)
```

```out
3
3.3039215686274517
16
```

Note that to `**` raises the first number to the power of the second.
