

# Generated at 2026-10-24 07:58:33.615344
# Unit test for function eat

# Generated at 2026-10-24 07:58:36.032207
# Unit test for function eat

# Generated at 2026-10-24 07:58:39.236483
# Unit test for function eat
def test_eat():assert module_0.eat(10, 5, 8) == [15, 3]

# Generated at 2026-10-24 07:58:40.671868
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(10, 5, 10) == [15, 5]
    # need == remaining
    assert module_0.eat(10, 10, 10) == [20, 0]
    # need > remaining
    assert module_0.eat(10, 10, 5) == [15, 0]
    # need == 0
    assert module_0.eat(7, 0, 5) == [7, 5]
    # remaining == 0
    assert module_0.eat(7, 5, 0) == [7, 0]
    # all zero
    assert module_0.eat(0, 0, 0) == [0, 0]

# Generated at 2026-10-24 07:58:42.019444
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(10, 5, 10) == [15, 5]
    # need == remaining
    assert module_0.eat(10, 10, 10) == [20, 0]
    # need > remaining
    assert module_0.eat(10, 10, 5) == [15, 0]
    # need == 0
    assert module_0.eat(7, 0, 5) == [7, 5]
    # remaining == 0
    assert module_0.eat(7, 5, 0) == [7, 0]
    # all zero
    assert module_0.eat(0, 0, 0) == [0, 0]

# Generated at 2026-10-24 07:58:43.434006
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(10, 5, 10) == [15, 5]
    # need == remaining
    assert module_0.eat(10, 10, 10) == [20, 0]
    # need > remaining
    assert module_0.eat(10, 10, 5) == [15, 0]
    # need == 0
    assert module_0.eat(7, 0, 5) == [7, 5]
    # remaining == 0
    assert module_0.eat(7, 5, 0) == [7, 0]
    # all zero
    assert module_0.eat(0, 0, 0) == [0, 0]

# Generated at 2026-10-24 07:58:44.801029
# Unit test for function eat
def test_eat():
    # need < remaining
    assert module_0.eat(10, 5, 10) == [15, 5]
    # need == remaining
    assert module_0.eat(10, 10, 10) == [20, 0]
    # need > remaining
    assert module_0.eat(10, 10, 5) == [15, 0]
    # need == 0
    assert module_0.eat(7, 0, 5) == [7, 5]
    # remaining == 0
    assert module_0.eat(7, 5, 0) == [7, 0]
    # all zero
    assert module_0.eat(0, 0, 0) == [0, 0]