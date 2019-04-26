def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "eight_factorial" in globals(), "Did you assign 8*...*1 to the variable eight_factorial?"
    assert "print(math.factorial(8))" in __solution__, "Are you using the `math.factorial` function?"

    __msg__.good("Well done!")
