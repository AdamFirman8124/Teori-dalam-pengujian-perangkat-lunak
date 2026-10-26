

# Generated at 2026-10-25 07:25:51.586954
# Unit test for function is_bored

# Generated at 2026-10-25 07:25:53.999861
# Unit test for function is_bored

# Generated at 2026-10-25 07:25:56.414081
# Unit test for function is_bored

# Generated at 2026-10-25 07:25:58.828631
# Unit test for function is_bored

# Generated at 2026-10-25 07:26:01.242325
# Unit test for function is_bored

# Generated at 2026-10-25 07:26:03.656612
# Unit test for function is_bored

# Generated at 2026-10-25 07:26:06.070302
# Unit test for function is_bored

# Generated at 2026-10-25 07:26:08.483741
# Unit test for function is_bored

# Generated at 2026-10-25 07:26:17.334352
# Unit test for function is_bored
def test_is_bored():assert module_0.is_bored("I am happy. You are sad. I am bored.") == 2

# Generated at 2026-10-25 07:26:18.769303
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

# Generated at 2026-10-25 07:26:20.100350
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