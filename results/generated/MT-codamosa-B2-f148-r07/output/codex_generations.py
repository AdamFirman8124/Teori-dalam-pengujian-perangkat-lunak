

# Generated at 2026-10-25 00:44:22.993847
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

# Generated at 2026-10-25 00:44:24.325058
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

# Generated at 2026-10-25 00:44:25.656026
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

# Generated at 2026-10-25 00:44:27.008591
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

# Generated at 2026-10-25 00:44:28.345653
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