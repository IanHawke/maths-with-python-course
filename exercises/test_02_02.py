def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "cuboid_volume" in globals(), "Did you call the function cuboid_volume?"
    assert callable(cuboid_volume), "Your cuboid_volume is not a valid function?"
    assert cuboid_volume(1, 1, 1)==1, "Your function gives errors when a=b=c=1 (should return 1)."
    assert cuboid_volume(1, 2, 3.5)==7, "Your function gives errors when a=1, b=2, c=3.5 (should return 7)."
    assert cuboid_volume(1, 0, 2)==0, "Your function gives errors when a=1, b=0, c=2 (should return 0)."

    __msg__.good("Well done!")
