

# Generated at 2026-10-25 14:08:26.212410
# Unit test for function is_bored
def test_is_bored():
    assert module_0.is_bored("I am bored.") == 1
    assert module_0.is_bored("I am bored. I am happy!") == 2
    assert module_0.is_bored("Hello. I am bored?") == 1
    assert module_0.is_bored("I am bored. You are bored.") == 1
    assert module_0.is_bored("I am bored...") == 1
    assert module_0.is_bored("I am bored.  I am happy.") == 2
    assert module_0.is_bored("This is I am bored.") == 0
    assert module_0.is_bored("i am bored.") == 0
    assert module_0.is_bored("I\tam bored.") == 0
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("") == 0

# Generated at 2026-10-25 14:08:27.586224
# Unit test for function is_bored
def test_is_bored():
    assert module_0.is_bored("I am bored.") == 1
    assert module_0.is_bored("I am bored. I am happy!") == 2
    assert module_0.is_bored("Hello. I am bored?") == 1
    assert module_0.is_bored("I am bored. You are bored.") == 1
    assert module_0.is_bored("I am bored...") == 1
    assert module_0.is_bored("I am bored.  I am happy.") == 2
    assert module_0.is_bored("This is I am bored.") == 0
    assert module_0.is_bored("i am bored.") == 0
    assert module_0.is_bored("I\tam bored.") == 0
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("") == 0

# Generated at 2026-10-25 14:08:29.077922
# Unit test for function is_bored
def test_is_bored():
    assert module_0.is_bored("I am bored.") == 1
    assert module_0.is_bored("I am bored. I am happy!") == 2
    assert module_0.is_bored("Hello. I am bored?") == 1
    assert module_0.is_bored("I am bored. You are bored.") == 1
    assert module_0.is_bored("I am bored...") == 1
    assert module_0.is_bored("I am bored.  I am happy.") == 2
    assert module_0.is_bored("This is I am bored.") == 0
    assert module_0.is_bored("i am bored.") == 0
    assert module_0.is_bored("I\tam bored.") == 0
    assert module_0.is_bored("I") == 0
    assert module_0.is_bored("") == 0

# Generated at 2026-10-25 14:08:37.450800
# Unit test for function is_bored
def test_is_bored():
    assert module_0.is_bored("I am bored.") == 1
    assert module_0.is_bored("I am bored. I want to leave!") == 2
    assert module_0.is_bored("You are bored. I am not?") == 1
    assert module_0.is_bored("You are bored! Are you leaving?") == 0
    assert module_0.is_bored("I am here!I am still here?I want to go.") == 3
    assert module_0.is_bored("") == 0

# Generated at 2026-10-25 14:08:48.641871
# Unit test for function is_bored
def test_is_bored():
    assert module_0.is_bored("I am bored. Are you?") == 1
    assert module_0.is_bored("I am bored. Are you? I am tired!") == 2
    assert module_0.is_bored("Are you bored? I am not. I am happy!") == 2
    assert module_0.is_bored("You said I am bored. I disagree.") == 1
    assert module_0.is_bored("i am bored. I am not.") == 1  # Case-sensitive
    assert module_0.is_bored("") == 0