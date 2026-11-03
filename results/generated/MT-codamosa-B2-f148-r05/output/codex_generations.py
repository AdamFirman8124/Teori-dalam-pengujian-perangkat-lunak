

# Generated at 2026-11-02 11:11:44.825596
# Unit test for function bf
def test_bf():
    # Valid planets: planet1 before planet2 in orbit order
    assert module_0.bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Earth", "Jupiter") == ("Mars",)
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # Valid planets: planet1 after planet2 (reversed order)
    assert module_0.bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Jupiter", "Earth") == ("Mars",)
    assert module_0.bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # Adjacent planets: nothing in between
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()
    assert module_0.bf("Jupiter", "Saturn") == ()

    # Same planet for both arguments
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Neptune", "Neptune") == ()

    # Invalid planet names
    assert module_0.bf("Pluto", "Earth") == ()
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("Foo", "Bar") == ()
    assert module_0.bf("mercury", "Venus") == ()  # case-sensitive
    assert module_0.bf("", "Mars") == ()

    # Result is a tuple
    assert isinstance(module_0.bf("Earth", "Saturn"), tuple)
    assert module_0.bf("Earth", "Saturn") == ("Mars", "Jupiter")

# Generated at 2026-11-02 11:14:06.493191
# Unit test for function bf
def test_bf():
    # Planets between Jupiter and Neptune (in order)
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    # Reversed order should still return planets in orbital order
    assert module_0.bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    # Planets between Earth and Mercury
    assert module_0.bf("Earth", "Mercury") == ("Venus",)
    # Adjacent planets -> nothing in between
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()
    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()
    # Invalid planet names -> empty tuple
    assert module_0.bf("Asculon", "Earth") == ()
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("foo", "bar") == ()
    # Wide range
    assert module_0.bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Venus", "Venus") == ()

# Generated at 2026-11-02 11:16:30.728143
# Unit test for function bf
def test_bf():
    # Planets between Jupiter and Neptune (exclusive)
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")

    # Reversed order should still return planets in order from the sun
    assert module_0.bf("Neptune", "Jupiter") == ("Saturn", "Uranus")

    # Adjacent planets yield empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()

    # Single planet in between
    assert module_0.bf("Earth", "Mercury") == ("Venus",)
    assert module_0.bf("Mercury", "Earth") == ("Venus",)

    # Full range between outermost planets
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # Invalid planet names return empty tuple
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("Pluto", "Earth") == ()
    assert module_0.bf("ASDF", "Venus") == ()
    assert module_0.bf("Venus", "ASDF") == ()

    # Same planet returns empty tuple
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Venus", "Venus") == ()

    # Case-sensitive invalid inputs
    assert module_0.bf("earth", "Mars") == ()
    assert module_0.bf("Mars", "earth") == ()

# Generated at 2026-11-02 11:18:28.582185
# Unit test for function bf
def test_bf():
    # Correct order (planet1 closer to the sun)
    assert module_0.bf("Earth", "Jupiter") == ("Mars",)
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert module_0.bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")

    # Reverse order (planet2 closer to the sun)
    assert module_0.bf("Jupiter", "Earth") == ("Mars",)
    assert module_0.bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert module_0.bf("Saturn", "Venus") == ("Earth", "Mars", "Jupiter")

    # Adjacent planets yield empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()
    assert module_0.bf("Uranus", "Neptune") == ()

    # Invalid planet names yield empty tuple
    assert module_0.bf("Pluto", "Earth") == ()
    assert module_0.bf("Earth", "Pluto") == ()
    assert module_0.bf("Xyz", "Abc") == ()

    # Same planet yields empty tuple
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Mercury", "Mercury") == ()

    # Case sensitivity: lowercase names are invalid
    assert module_0.bf("earth", "Mars") == ()
    assert module_0.bf("Earth", "mars") == ()