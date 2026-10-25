

# Generated at 2026-10-24 14:12:44.213887
# Unit test for function is_bored
def test_is_bored():
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("I am bored.") == 1
    assert module_0.is_bored("The sky is blue. I love this weather.") == 1
    assert module_0.is_bored("I am bored. I am still bored? I am very bored!") == 3
    assert module_0.is_bored("I am bored?You are not!I am tired.") == 2
    assert module_0.is_bored("Hello. I am here! Are you? I am bored.") == 2
    # "I" must be a separate word: "Ice" does not count
    assert module_0.is_bored("Ice cream is tasty. I like it.") == 1
    # case-sensitive: lowercase "i" does not count
    assert module_0.is_bored("i am bored. I am bored.") == 1
    # no boredom
    assert module_0.is_bored("You are bored. He is bored.") == 0

# Generated at 2026-10-24 14:12:51.405136
# Unit test for function is_bored
def test_is_bored():
    # Basic cases
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it") == 1

    # Multiple boredoms across sentences
    assert module_0.is_bored("I feel bored. I want to sleep. You are fine.") == 2

    # Delimiters: . ? !
    assert module_0.is_bored("I am bored? I am sleepy! I am hungry.") == 3

    # "Is" and "It" must NOT count â only "I " as first word
    assert module_0.is_bored("Is the sky blue? It is.") == 0

    # Empty and edge cases
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I") == 0          # single "I" with no following word/space
    assert module_0.is_bored("I love it.") == 1  # trailing delimiter is fine

    # Leading/trailing whitespace
    assert module_0.is_bored("  I am tired.") == 1

    print("All tests passed!")


test_is_bored()

# Generated at 2026-10-24 14:12:53.099622
# Unit test for function is_bored
def test_is_bored():
    # Basic cases
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it") == 1

    # Multiple boredoms across sentences
    assert module_0.is_bored("I feel bored. I want to sleep. You are fine.") == 2

    # Delimiters: . ? !
    assert module_0.is_bored("I am bored? I am sleepy! I am hungry.") == 3

    # "Is" and "It" must NOT count â only "I " as first word
    assert module_0.is_bored("Is the sky blue? It is.") == 0

    # Empty and edge cases
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I") == 0          # single "I" with no following word/space
    assert module_0.is_bored("I love it.") == 1  # trailing delimiter is fine

    # Leading/trailing whitespace
    assert module_0.is_bored("  I am tired.") == 1

    print("All tests passed!")


test_is_bored()

# Generated at 2026-10-24 14:12:54.429379
# Unit test for function is_bored
def test_is_bored():
    # Basic cases
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it") == 1

    # Multiple boredoms across sentences
    assert module_0.is_bored("I feel bored. I want to sleep. You are fine.") == 2

    # Delimiters: . ? !
    assert module_0.is_bored("I am bored? I am sleepy! I am hungry.") == 3

    # "Is" and "It" must NOT count â only "I " as first word
    assert module_0.is_bored("Is the sky blue? It is.") == 0

    # Empty and edge cases
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I") == 0          # single "I" with no following word/space
    assert module_0.is_bored("I love it.") == 1  # trailing delimiter is fine

    # Leading/trailing whitespace
    assert module_0.is_bored("  I am tired.") == 1

    print("All tests passed!")


test_is_bored()

# Generated at 2026-10-24 14:12:55.763009
# Unit test for function is_bored
def test_is_bored():
    # Basic cases
    assert module_0.is_bored("Hello world") == 0
    assert module_0.is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert module_0.is_bored("I love it") == 1

    # Multiple boredoms across sentences
    assert module_0.is_bored("I feel bored. I want to sleep. You are fine.") == 2

    # Delimiters: . ? !
    assert module_0.is_bored("I am bored? I am sleepy! I am hungry.") == 3

    # "Is" and "It" must NOT count â only "I " as first word
    assert module_0.is_bored("Is the sky blue? It is.") == 0

    # Empty and edge cases
    assert module_0.is_bored("") == 0
    assert module_0.is_bored("I") == 0          # single "I" with no following word/space
    assert module_0.is_bored("I love it.") == 1  # trailing delimiter is fine

    # Leading/trailing whitespace
    assert module_0.is_bored("  I am tired.") == 1

    print("All tests passed!")


test_is_bored()