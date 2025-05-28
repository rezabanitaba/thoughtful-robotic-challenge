
def test_sort():
    # Standard package
    assert sort(100, 100, 100, 10) == "STANDARD"

    # Bulky due to volme
    assert sort(200, 200, 200, 10) == "SPECIAL"

    # Bulky due to dimension
    assert sort(150, 50, 50, 10) == "SPECIAL"

    # Heavy only
    assert sort(100, 100, 100, 25) == "SPECIAL"

    # Bulky and heavy
    assert sort(160, 160, 160, 30) == "REJECTED"

    # just below bulky and heavy
    assert sort(149, 149, 149, 19.9) == "STANDARD"

    # edge case test: exactly on bulky dimension and heavy mass
    assert sort(150, 50, 50, 20) == "REJECTED"

    print("All tests OK")

test_sort()
