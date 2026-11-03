

# Generated at 2026-11-02 17:58:51.548404
# Unit test for function bf
def test_bf():
    # Planets in forward order (planet1 closer to Sun than planet2)
    assert module_0.bf("Earth", "Jupiter") == ("Mars",)
    assert module_0.bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Venus", "Mars") == ("Earth",)
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # Planets in reverse order (planet2 closer to Sun than planet1)
    assert module_0.bf("Jupiter", "Earth") == ("Mars",)
    assert module_0.bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # Adjacent planets - nothing in between
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()
    assert module_0.bf("Mercury", "Venus") == ()

    # Same planet returns empty tuple
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Neptune", "Neptune") == ()

    # Invalid planet names return empty tuple
    assert module_0.bf("Pluto", "Earth") == ()
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("foo", "bar") == ()
    assert module_0.bf("", "Mars") == ()

    # Case sensitivity - invalid lowercase names
    assert module_0.bf("earth", "Mars") == ()
    assert module_0.bf("Earth", "mars") == ()

# Generated at 2026-11-02 18:00:26.513620
# Unit test for function bf
def test_bf():
    # Planets between Jupiter and Neptune
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    # Reversed order works too
    assert module_0.bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    # Single planet in between
    assert module_0.bf("Venus", "Mars") == ("Earth",)
    assert module_0.bf("Mars", "Venus") == ("Earth",)
    # Multiple planets in between
    assert module_0.bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Earth", "Neptune") == ("Mars", "Jupiter", "Saturn", "Uranus")
    # Adjacent planets -> empty tuple
    assert module_0.bf("Mercury", "Venus") == ()
    assert module_0.bf("Saturn", "Uranus") == ()
    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Neptune", "Neptune") == ()
    # Invalid planet names -> empty tuple
    assert module_0.bf("Pluto", "Mars") == ()
    assert module_0.bf("Mars", "Pluto") == ()
    assert module_0.bf("Foo", "Bar") == ()
    # Case sensitivity: invalid inputs
    assert module_0.bf("earth", "Mars") == ()
    assert module_0.bf("Earth", "mars") == ()

# Generated at 2026-11-02 18:02:06.710586
# Unit test for function bf
def test_bf():
    # Planets between Jupiter and Neptune (in orbital order)
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    # Reversed argument order returns the same planets
    assert module_0.bf("Neptune", "Jupiter") == ("Saturn", "Uranus")

    # Planets between Mercury and Mars
    assert module_0.bf("Mercury", "Mars") == ("Venus", "Earth")

    # Reversed: Mars to Mercury
    assert module_0.bf("Mars", "Mercury") == ("Venus", "Earth")

    # Adjacent planets — nothing in between
    assert module_0.bf("Earth", "Mars") == ()

    # Same planet for both arguments — empty tuple
    assert module_0.bf("Earth", "Earth") == ()

    # One or both planet names invalid — empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("Xena", "Mars") == ()
    assert module_0.bf("", "") == ()

    # Names are case-sensitive
    assert module_0.bf("earth", "Mars") == ()
    assert module_0.bf("Earth", "mars") == ()

    # Full span between Mercury and Neptune
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # Result type is always a tuple
    result = module_0.bf("Venus", "Saturn")
    assert isinstance(result, tuple)
    assert result == ("Earth", "Mars", "Jupiter")

    print("All tests passed!")


test_bf()

# Generated at 2026-11-02 18:04:26.742260
# Unit test for function bf
def test_bf():
    # Planets between two valid planets (planet1 before planet2)
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Earth", "Mars") == ("Venus",) is False or module_0.bf("Earth", "Mars") == ("Venus",)

    # Reversed order (planet2 before planet1)
    assert module_0.bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    assert module_0.bf("Venus", "Mercury") == ()

    # Adjacent planets return an empty tuple
    assert module_0.bf("Mercury", "Venus") == ()
    assert module_0.bf("Uranus", "Neptune") == ()

    # Same planet returns empty tuple
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Mars", "Mars") == ()

    # Invalid planet names return empty tuple
    assert module_0.bf("earth", "Earth") == ()
    assert module_0.bf("Jupiter", "Pluto") == ()
    assert module_0.bf("foo", "Bar") == ()
    assert module_0.bf("", "Earth") == ()
    assert module_0.bf("Earth", "") == ()

    # Case sensitivity checks
    assert module_0.bf("MERCURY", "VENUS") == ()
    assert module_0.bf("Mercury", "venus") == ()

    # Full range check
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert module_0.bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    print("All tests passed!")

# Generated at 2026-11-02 18:06:04.409262
# Unit test for function bf
def test_bf():
    # Planets between, in forward order
    assert module_0.bf("Earth", "Jupiter") == ("Mars",)
    assert module_0.bf("Venus", "Mars") == ("Earth",)
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # Planets between, in reverse order (order of args shouldn't matter)
    assert module_0.bf("Jupiter", "Earth") == ("Mars",)
    assert module_0.bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert module_0.bf("Mars", "Venus") == ("Earth",)

    # Adjacent planets -> no planets in between
    assert module_0.bf("Mercury", "Venus") == ()
    assert module_0.bf("Venus", "Mercury") == ()
    assert module_0.bf("Uranus", "Neptune") == ()

    # Same planet -> invalid
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Neptune", "Neptune") == ()

    # Invalid planet names
    assert module_0.bf("Pluto", "Earth") == ()
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("Sun", "Moon") == ()
    assert module_0.bf("", "Earth") == ()

    # Case sensitivity
    assert module_0.bf("earth", "mars") == ()
    assert module_0.bf("Earth", "mars") == ()

    # Non-string inputs
    assert module_0.bf(1, 2) == ()
    assert module_0.bf(None, "Earth") == ()

    # Result is always a tuple
    result = module_0.bf("Earth", "Saturn")
    assert isinstance(result, tuple)
    assert result == ("Mars", "Jupiter")

    print("All tests passed!")