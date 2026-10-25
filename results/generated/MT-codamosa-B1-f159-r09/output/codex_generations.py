

# Generated at 2026-10-24 15:08:51.894287
# Unit test for function eat

# Generated at 2026-10-24 15:08:54.309778
# Unit test for function eat

# Generated at 2026-10-24 15:08:56.723304
# Unit test for function eat

# Generated at 2026-10-24 15:08:59.137290
# Unit test for function eat

# Generated at 2026-10-24 15:09:01.551310
# Unit test for function eat

# Generated at 2026-10-24 15:09:03.962884
# Unit test for function eat

# Generated at 2026-10-24 15:09:06.374872
# Unit test for function eat

# Generated at 2026-10-24 15:09:08.788699
# Unit test for function eat

# Generated at 2026-10-24 15:09:18.007511
# Unit test for function eat
def test_eat():assert module_0.eat(5, 3, 10) == [8, 7]

# Generated at 2026-10-24 15:09:19.606956
# Unit test for function eat
def test_eat():
    # need <= remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(4, 8, 9) == [12, 1]

    # need == remaining
    assert module_0.eat(1, 10, 10) == [11, 0]

    # need > remaining -> eat all remaining
    assert module_0.eat(2, 11, 5) == [7, 0]

# Generated at 2026-10-24 15:09:21.248396
# Unit test for function eat
def test_eat():
    # need <= remaining
    assert module_0.eat(5, 6, 10) == [11, 4]
    assert module_0.eat(4, 8, 9) == [12, 1]

    # need == remaining
    assert module_0.eat(1, 10, 10) == [11, 0]

    # need > remaining -> eat all remaining
    assert module_0.eat(2, 11, 5) == [7, 0]