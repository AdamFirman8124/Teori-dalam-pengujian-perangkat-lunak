

# Generated at 2026-10-25 02:18:39.950894
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

# Generated at 2026-10-25 02:18:41.387198
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

# Generated at 2026-10-25 02:18:42.713036
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

# Generated at 2026-10-25 02:18:44.148236
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

# Generated at 2026-10-25 02:18:46.668347
# Unit test for function bf

# Generated at 2026-10-25 02:18:49.196122
# Unit test for function bf

# Generated at 2026-10-25 02:18:51.614610
# Unit test for function bf