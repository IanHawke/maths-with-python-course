---
title: 'Chapter 1: Getting started'
description:
  'This chapter will teach you using Python as a calculator'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Introduction" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>

<exercise id="2" title="Printing">

How can you make Python display the result of 4! to the screen?

<choice>
<opt text="print 4*3*2*1">

This will not work. In modern Python, `print` is a function. You must put its
argument inside brackets.

</opt>

<opt text="print(3*2*2)" correct="true">

Correct! This is, of course, a silly way of writing `print(4*3*2*1)`.

</opt>

<opt text="print(4*3*1*1)">

This is wrong: read the argument passed in carefully.

</opt>
</choice>

</exercise>

<exercise id="3" title="Variables" type="slides">

<slides source="chapter1_03_variables">
</slides>

</exercise>

<exercise id="4" title="Good variables">

An object is dropped from height $H$ at time $0$. Its height at time $t$ is given by
$$
  h(t) = H - \tfrac{1}{2} g t^2.
$$
What would be a good set of variables to use for this expression?

<choice>

<opt text="h = H - g * t**2 / 2">
This isn't bad as it mirrors the mathematical form. However, it's not the best, as you need to have the mathematical form and explanation along with the code to understand it.
</opt>

<opt text="height = initial height - gravity constant * time**2 / 2">
  This will fail as Python variables cannot contain spaces, so "initial height" and "gravity constant" are not valid syntax.
</opt>

<opt text="height = initial_height - gravity_constant * time**2 / 2" correct="true">
  This is very verbose but clear without any additional explanation.
</opt>

</choice>

</exercise>

<exercise id="5" title="Packages" type="slides">

<slides source="chapter1_04_packages">
</slides>

</exercise>

<exercise id="6" title="Factorials">

Calculate 8! by explicitly multiplying all integers from 1 to 8 and assign the
result to the variable `eight_factorial`. Use the appropriate function from the
`math` library to check that the numbers match. Check the output when you
directly compare the values using `==`.

<codeblock id="01_05">

The function from `math` providing the factorial is `math.factorial`. It takes
one argument - the number whose factorial is to be returned.

</codeblock>

</exercise>
