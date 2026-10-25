

# Generated at 2026-10-25 01:06:50.549757
# Unit test for function bf

# Generated at 2026-10-25 01:06:52.964689
# Unit test for function bf

# Generated at 2026-10-25 01:06:55.402427
# Unit test for function bf

# Generated at 2026-10-25 01:06:57.961005
# Unit test for function bf

# Generated at 2026-10-25 01:07:00.375705
# Unit test for function bf

# Generated at 2026-10-25 01:07:02.790033
# Unit test for function bf

# Generated at 2026-10-25 01:07:05.205230
# Unit test for function bf

# Generated at 2026-10-25 01:07:07.620580
# Unit test for function bf

# Generated at 2026-10-25 01:07:10.038359
# Unit test for function bf

# Generated at 2026-10-25 01:07:12.453571
# Unit test for function bf

# Generated at 2026-10-25 01:07:14.871481
# Unit test for function bf

# Generated at 2026-10-25 01:07:17.287289
# Unit test for function bf

# Generated at 2026-10-25 01:07:19.706809
# Unit test for function bf

# Generated at 2026-10-25 01:07:24.523593
# Unit test for function bf
def test_bf():assert module_0.bf("Mercury", "Jupiter") == ("Venus", "Earth", "Mars")

# Generated at 2026-10-25 01:07:25.957834
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:27.265044
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:28.583863
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:29.917301
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:31.290011
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:32.609579
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:33.924114
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:35.240916
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:36.576844
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()

# Generated at 2026-10-25 01:07:37.910622
# Unit test for function bf
def test_bf():
    # Normal cases, both directions
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Jupiter") == ("Uranus", "Saturn")
    assert module_0.bf("Earth", "Mercury") == ("Venus",)

    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Invalid inputs -> empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("ASDF", "Earth") == ()
    assert module_0.bf("earth", "Mars") == ()   # case-sensitive

    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # Full range
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars",
                                        "Jupiter", "Saturn", "Uranus")

    # Return type must be a tuple
    assert isinstance(module_0.bf("Earth", "Jupiter"), tuple)

    print("All tests passed.")


test_bf()