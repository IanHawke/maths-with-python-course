---
type: slides
---

# Packages

Notes: We saw Python as a basic calculator. There's more complex mathematical operations that we want to do, however.

---

# Mathematical operations

Base Python doesn't do interesting maths:

```python
# Print something
print(sin(1))
```

```out
NameError: name 'sin' is not defined
```

More functions can be found in *packages*, and accessed using `import`:

```python
import math
print(math.sin(1))
```

```out
0.8414709848078965
```

Notes: Base Python will do arithmetic, but doesn't have much else. To extend the features available, people write packages containing functions and structures. The `import` command gives us access to the contents of the package. We access things (functions, structures, values, etc) using the name of the package (here `math`) followed by a dot, then the name of the thing (here the function `sin`). This notation is lengthy, but it's very useful in maths and science where the same few letters are often used for different things. For example, think about how `e` can be both the mathematical constant 2.71828... or the charge of the electron. Compare their values by looking at `math.e` and `scipy.constants.e` (you'll have to import the modules first!).

---

# Let's practice!

Notes: Move on to some exercises.
