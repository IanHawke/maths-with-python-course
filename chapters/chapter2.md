---
title: 'Chapter 2: Functions'
description:
  'This chapter will teach you about functions, and how mathematical and computational versions differ.'
prev: /chapter1
next: /chapter3
type: chapter
id: 2
---

<exercise id="1" title="Introduction" type="slides">

<slides source="chapter2_01_introduction">
</slides>

</exercise>

<exercise id="2" title="Cuboid volume">

Write a function `cuboid_volume` to calculate the volume of a cuboid box. The inputs should be the edge lengths of the cuboid, $a, b, c$. The output should be the volume $a \times b \times c$.

<codeblock id="02_02">

We will talk later about what it means for a function to have multiple inputs and multiple outputs.

</codeblock>

</exercise>

<exercise id="3" title="Documentation" type="slides">

<slides source="chapter2_03_documentation">
</slides>

</exercise>


<exercise id="4" title="Good documentation">

An object is dropped from height $H$ at time $0$. Its height at time $t$ is given by
$$
  h(t) = H - \tfrac{1}{2} g t^2.
$$
A function to compute the height at a given time is

```python
def drop_height(initial_height, time):
  return initial_height - 1 / 2 * 9.81 * time**2
```

Which of the following should **not** be documented?

<choice>

<opt text="What the units are.">
  This is essential to understand the output. Here we have the gravitational constant in SI units: we'd get very different results if height was in feet and time in days.
</opt>

<opt text="What happens if the initial height is negative.">
  This may not be essential, but could explain what you are thinking. If h=0 means "the ground" then H negative makes no sense, and should be an error. If h=0 means "some arbitrary point", like the top of a building, then there's nothing wrong with H negative. Here we're implicitly using the latter.
</opt>

<opt text="Who wrote the function." correct="true">
  Some people do want to document who did what, so that the author can be thanked, blamed, or asked to fix something. In modern Python that is not the preferred convention, so this should not be documented within the code.
</opt>

<opt text="None of the above - all should be documented.">
  One of the above doesn't tell you how the function should be used, or how its inputs or results should be interpreted.
</opt>

</choice>

</exercise>


<exercise id="5" title="Scope" type="slides">

<slides source="chapter2_05_scope">
</slides>

</exercise>
