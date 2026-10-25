

# Generated at 2026-10-25 00:24:54.113815
# Unit test for function bf

# Generated at 2026-10-25 00:24:56.545496
# Unit test for function bf

# Generated at 2026-10-25 00:24:58.987770
# Unit test for function bf

# Generated at 2026-10-25 00:25:01.430611
# Unit test for function bf

# Generated at 2026-10-25 00:25:03.857791
# Unit test for function bf

# Generated at 2026-10-25 00:25:06.271925
# Unit test for function bf

# Generated at 2026-10-25 00:25:08.688403
# Unit test for function bf

# Generated at 2026-10-25 00:25:11.101932
# Unit test for function bf

# Generated at 2026-10-25 00:25:13.515733
# Unit test for function bf

# Generated at 2026-10-25 00:25:15.931753
# Unit test for function bf

# Generated at 2026-10-25 00:25:18.347273
# Unit test for function bf

# Generated at 2026-10-25 00:25:20.760293
# Unit test for function bf

# Generated at 2026-10-25 00:25:28.424822
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