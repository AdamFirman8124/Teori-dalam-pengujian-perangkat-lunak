

# Generated at 2026-10-25 06:16:19.893582
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

# Generated at 2026-10-25 06:16:21.272434
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

# Generated at 2026-10-25 06:16:22.717166
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

# Generated at 2026-10-25 06:16:24.240583
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

# Generated at 2026-10-25 06:16:25.809348
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