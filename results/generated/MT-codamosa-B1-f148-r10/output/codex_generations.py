

# Generated at 2026-10-25 02:29:23.032535
# Unit test for function bf

# Generated at 2026-10-25 02:29:25.672002
# Unit test for function bf

# Generated at 2026-10-25 02:29:28.233410
# Unit test for function bf

# Generated at 2026-10-25 02:29:30.773274
# Unit test for function bf

# Generated at 2026-10-25 02:29:33.191152
# Unit test for function bf

# Generated at 2026-10-25 02:29:35.607563
# Unit test for function bf

# Generated at 2026-10-25 02:29:38.021228
# Unit test for function bf

# Generated at 2026-10-25 02:29:40.436204
# Unit test for function bf

# Generated at 2026-10-25 02:29:42.853271
# Unit test for function bf

# Generated at 2026-10-25 02:29:45.270575
# Unit test for function bf

# Generated at 2026-10-25 02:29:47.687075
# Unit test for function bf

# Generated at 2026-10-25 02:29:50.106188
# Unit test for function bf

# Generated at 2026-10-25 02:29:52.521557
# Unit test for function bf

# Generated at 2026-10-25 02:29:54.943216
# Unit test for function bf

# Generated at 2026-10-25 02:29:57.372599
# Unit test for function bf

# Generated at 2026-10-25 02:29:59.792380
# Unit test for function bf

# Generated at 2026-10-25 02:30:03.781622
# Unit test for function bf
def test_bf():assert module_0.bf("Earth", "Mercury") == ("Venus",)

# Generated at 2026-10-25 02:30:05.144914
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

# Generated at 2026-10-25 02:30:06.498616
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

# Generated at 2026-10-25 02:30:07.862248
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

# Generated at 2026-10-25 02:30:09.197638
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

# Generated at 2026-10-25 02:30:10.526992
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

# Generated at 2026-10-25 02:30:11.859239
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

# Generated at 2026-10-25 02:30:13.173270
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

# Generated at 2026-10-25 02:30:14.490741
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

# Generated at 2026-10-25 02:30:15.820775
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