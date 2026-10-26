

# Generated at 2026-10-25 07:12:07.343132
# Unit test for function bf

# Generated at 2026-10-25 07:12:09.952981
# Unit test for function bf

# Generated at 2026-10-25 07:12:12.367313
# Unit test for function bf

# Generated at 2026-10-25 07:12:14.783098
# Unit test for function bf

# Generated at 2026-10-25 07:12:17.199487
# Unit test for function bf

# Generated at 2026-10-25 07:12:19.614358
# Unit test for function bf

# Generated at 2026-10-25 07:12:22.183950
# Unit test for function bf

# Generated at 2026-10-25 07:12:24.513815
# Unit test for function bf

# Generated at 2026-10-25 07:12:26.928852
# Unit test for function bf

# Generated at 2026-10-25 07:12:35.609908
# Unit test for function bf
def test_bf():
    # Planets between, forward order
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    # Planets between, reverse order (arguments swapped)
    assert module_0.bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    # Adjacent planets -> empty tuple
    assert module_0.bf("Earth", "Mars") == ()
    assert module_0.bf("Mars", "Earth") == ()
    # Same planet -> empty tuple
    assert module_0.bf("Earth", "Earth") == ()
    # Invalid planet name -> empty tuple
    assert module_0.bf("Mercy", "Earth") == ()
    assert module_0.bf("Earth", "Pluto") == ()
    # Both invalid -> empty tuple
    assert module_0.bf("Foo", "Bar") == ()
    # Full span: everything between Mercury and Neptune
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert module_0.bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    # Single planet between
    assert module_0.bf("Earth", "Mercury") == ("Venus",)
    assert module_0.bf("Mercury", "Earth") == ("Venus",)
    # Case sensitivity: wrong case is invalid
    assert module_0.bf("earth", "mars") == ()

# Generated at 2026-10-25 07:12:37.005012
# Unit test for function bf
def test_bf():
    # planets between - normal order
    assert module_0.bf("Mercury", "Earth") == ("Venus",)
    assert module_0.bf("Earth", "Jupiter") == ("Mars",)
    assert module_0.bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert module_0.bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert module_0.bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # reversed order should give same result
    assert module_0.bf("Earth", "Mercury") == ("Venus",)
    assert module_0.bf("Jupiter", "Earth") == ("Mars",)
    assert module_0.bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
    assert module_0.bf("Neptune", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")

    # adjacent planets -> empty
    assert module_0.bf("Mercury", "Venus") == ()
    assert module_0.bf("Venus", "Mercury") == ()
    assert module_0.bf("Earth", "Mars") == ()

    # same planet -> empty
    assert module_0.bf("Earth", "Earth") == ()
    assert module_0.bf("Mars", "Mars") == ()

    # invalid names -> empty
    assert module_0.bf("Mercury", "Pluto") == ()
    assert module_0.bf("Pluto", "Mercury") == ()
    assert module_0.bf("Pluto", "Pluto") == ()
    assert module_0.bf("earth", "Mars") == ()
    assert module_0.bf("", "Earth") == ()